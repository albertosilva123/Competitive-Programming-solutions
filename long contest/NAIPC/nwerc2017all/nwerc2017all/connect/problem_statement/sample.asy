unitsize(1cm);

int[][] nums = {
	{1, 2, 3, 4},
	{10, 11, 12, 5},
	{9, 16, 6, 13},
	{8, 7, 15, 14},
};

for (int y = 0; y < 4; ++y) {
	for (int x = 0; x < 4; ++x) {
		fill(circle((x, 3 - y), 0.05));
		label("\small $" + string(nums[y][x]) + "$", (x - 0.2, 3 - y + 0.2));
	}
}

draw(
		(0, 3) --
		(4, 3) --
		(0, -1) --
		(0, 2) --
		(3, 2) --
		(3, -1) --
		(1, 1)
);
