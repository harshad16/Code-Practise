/*
https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/tile-stacking-problem/problem
We need to calculate the number of non-increasing i.e number of decreasing sequences of length  using numbers from  to  using each number at most  times.
The most straightforward solution is a recursive solution considering all the possibilities i.e. considering all possible sequences of length n using m numbers.This would definitely exceed the given time limit.
Consider the following dynamic programming solution with the following states:  where denotes the number of decreasing sequences of length  using numbers from  to . We need to take care of the fact that a number can be used a most  times. This can be done by considering  to  occurences of a number. Hence our recurrence relation becomes :
The time complexity of this solution is O(n*m*K). But, unfortunately this would not fit in given time limit.
We can use the fact that for a fixed  we are using the consecutive values of previous  values of . Hence, we can maintain a prefix sum array for each state. Now we have got rid of the  factor for each state. Hence the time complexity now reduces to O(n*K).
*/
#include <bits/stdc++.h>
using namespace std;

#define mi 1000000007
#define rep(i,a,b) for(i=a;i<b;i++)

int dp[1005][10005],presum[1005][10005];
inline int mod(int x) {
	return (x+mi)%mi;
} 
int main() {
	int n,m,k,i,j;
	scanf("%d",&n); scanf("%d",&m); scanf("%d",&k);
	//dp[i][j]-> i-number and j length
	rep(i,1,n+1) dp[0][i]=0,presum[0][i]=1;
	rep(i,0,m+1) presum[i][0]=dp[i][0]=1;
	rep(i,1,m+1) {
		rep(j,1,n+1) {
			dp[i][j]=presum[i-1][j];
			if(j>k) {
				dp[i][j]-=presum[i-1][j-k-1];
				dp[i][j]=mod(dp[i][j]);
			}
		}
		rep(j,1,n+1)
			presum[i][j]=(dp[i][j]+presum[i][j-1])%mi;
	}
	printf("%lld\n",dp[m][n]);
	return 0;
}