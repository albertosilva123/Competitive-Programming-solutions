#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <numeric>
#include <iomanip>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const double PI = 2.0 * acos(0.0);


typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORS(i,a,b,s) for (int i = (a); i < (b); i=i+(s))
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

string dut[30];
ull any[30];
map<string,int> yes;
map<string,int> no;

map<string,string> trans;

int main(){
	int n; cin >> n;
	FOR(i,0,n) cin >> dut[i];
	int m; cin >> m;
	FOR(i,0,m){
		string a,b,c; cin >> a >> b >> c;
		trans[a] = b;
		if (c == "correct") yes[a]++; else no[a]++;
	}
	// compute num
	any[n] = 1;
	FORD(i,0,n){
		any[i] = any[i+1] * (yes[dut[i]] + no[dut[i]]);
	}
	
	ll corr = 1;
	ll incor = 0;
	FOR(i,0,n) {
		incor += corr * no[dut[i]] * any[i+1];
		corr *= yes[dut[i]];
	}

	if (corr + incor == 1){
		FOR(i,0,n) cout << (i?" ":"") << trans[dut[i]];
	   	cout << endl;	
		if (corr) cout << "correct"; else cout << "incorrect";
		cout << endl;
	} else {
		cout << corr << " correct " << endl;
		cout << incor << " incorrect " << endl;
	}
}