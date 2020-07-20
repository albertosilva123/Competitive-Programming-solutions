#include "header_ragnar.h"

// usage: output_validator testcase.in testcase.ans < team_output

long double PRECISION = 0.100000000001L;

constexpr int ACCEPTED     = 42;
constexpr int WRONG_ANSWER = 43;

// input streams; also command line input
// - the .in file for the problem
// - the .ans file the problem
// - the .out generated by the submitted program
std::ifstream in, ans;
std::istream &out = std::cin;

// output streams:
// - message: how/why did the submitted position fail
// - error: this program is not behaving as it should
std::ostream &message = std::cerr;
std::ostream &error   = std::cerr;

int main(int argc, const char *args[]) {
	assert(argc == 3);

	in  = std::ifstream(args[1]);
	ans = std::ifstream(args[2]);

	// read answer
	Position answer;
	ans >> answer;

	// error << "read position\n";
	// TODO: This needs hardening against unexpected input!
	Position position;
	out >> position;

	// error << "read input\n";
	Input input;
	in >> input;

	auto tmp = make_image(input.params, position);
	if(tmp.second) return WRONG_ANSWER;
	auto &position_image = tmp.first;
	auto max_diff        = compare_images(input.image, position_image);
	if(max_diff > PRECISION) {
		message << std::setprecision(10) << std::fixed;
		message << "The max difference between input image and given position image is: "
		        << max_diff << "\n";

		message << "params: " << input.params.pixels << ' ' << input.params.theta << '\n';
		message << "reference position " << answer.p.x << ' ' << answer.p.y << ' ' << answer.alpha
		        << '\n';
		message << "answer position " << position.p.x << ' ' << position.p.y << ' '
		        << position.alpha << '\n';

		message << "First (at most) 10 mistakes: \n";
		int diffcount = 10;
		for(int i = 0; i < input.params.pixels; ++i) {
			ld maxdiff = 0;
			for(int j = 0; j < 3; ++j)
				maxdiff = std::max(maxdiff, std::abs(input.image[i][j] - position_image[i][j]));
			if(maxdiff > 0.0001) {
				message << i << ": ";
				for(int j = 0; j < 3; ++j) message << input.image[i][j] << ' ';
				message << '\t';
				for(int j = 0; j < 3; ++j) message << position_image[i][j] << ' ';
				message << '\n';
				++diffcount;
				if(diffcount > 10) break;
			}
		}
		return WRONG_ANSWER;
	}

	return ACCEPTED;
}
