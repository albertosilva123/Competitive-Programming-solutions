/*
	task:           Finding the number of simple paths in the 
					directed graph G = <V, E>.

	complexity:     O(f)
	
	notes:          Let dp[msk][v] be the number of Hamiltonian 
					walks in the subgraph generated by vertices 
					in msk that end in v.
*/

#define     BIT(n)  (1 << n)
const int   MAXN = 20;

int n, m, u, v, ans, g[MAXN], dp[BIT(MAXN)][MAXN];

int main()
{
	cin >> n >> m;
	
	for (int i = 0; i < m; ++i)
	{
		cin >> u >> v;
		g[u] |= BIT(v);
	}
	
	for (int i = 0; i < n; ++i)
	    dp[BIT(i)][i] = 1;
	
	for (int msk = 1; msk < BIT(n); ++msk)
	{
		for (int i = 0; i < n; ++i) if (BIT(i) & msk)
		{
			int tmsk = msk ^ BIT(i);
			
			for (int j = 0; tmsk && j < n; ++j) if (g[j] & BIT(i))
			    dp[msk][i] += dp[tmsk][j];
			    
			ans += dp[msk][i];
		}
	}
	cout << ans - n << endl;
	return 0;
}