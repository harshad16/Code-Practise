/*
https://www.hackerrank.com/contests/morgan-stanley-codeathon-2017/challenges/dreamplay-and-clubbing/problem
DP[i][j][k][t] denotes number of pairs, with above condition such that i most significant digits from left have been seen, 
difference between digit sums of first and second number is j, k = 0 denotes that the second number already has become smaller than N 
after considering most significant i digits, k = 1 denotes that the second number is equal to N, if most significant i digits are considered, 
t = 0 denotes that first number has become smaller than second after comparing i most significant digits and t = 1 denotes that first and second 
number are still equal if only i most significant digits are considered. For every state, we iterate over all the 10 * 10 digit combinations.
*/

#include<bits/stdc++.h>

using namespace std;


#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
  cerr << name << " : " << arg1 << endl;
}

template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << " : " << arg1<<" | ";
  __f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define all(a) a.begin(), a.end()
#define endl '\n'
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define boost  ios_base::sync_with_stdio(false);
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

typedef long long llint;
typedef long long ll ;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

const int mod = 1e9 + 7 ;
ll powmod(ll a,ll b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
ll gcd(ll a , ll b){return a==0?b:gcd(b%a,a);}
/*---------------------------------------------------------------------------------------------------------------------*/
const int maxn = 100010;
const int inf = INT_MAX;
string s;
const int N = 260;
int dp[N][N * 10 * 2][2][2];
int base = 10 * N;

ll solve(int idx, int dif, int fs, int sn) {


	if(fs == 2 || sn == 2)
		return 0;

	if(dp[idx][dif][fs][sn] != -1)
		return dp[idx][dif][fs][sn];

	if(idx == s.length()) {
		if(fs == 1 && dif - base > 0)
			return 1;
		return 0;
	}

	ll ans = 0;

	for(int i = 0; i < 10; i++)
	for(int j = 0; j < 10; j++) {

		int ndif = dif + j - i;

		int nfs = fs;
		if(fs == 0) {
			if(i < j)
				nfs = 1;
			else if(i == j)
				nfs = 0;
			else
				continue;
		}

		int nsn = sn;
		if(sn == 0) {
			if(j < s[idx] - '0')
				nsn = 1;
			else if(j == s[idx] - '0')
				nsn = 0;
			else
				continue;
		}

		ans = ans + solve(idx + 1, ndif, nfs, nsn);
	}
	if(ans >= mod)
		ans = ans % mod;

	return dp[idx][dif][fs][sn] = ans;

}

int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	memset(dp, -1, sizeof dp);
	cin >> s;
	ll ans = solve(0, 0 + base, 0, 0);
	cout << ans;

    return 0;
}