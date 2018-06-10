/* 
https://www.hackerrank.com/contests/morgan-stanley-codeathon-2017/challenges/football-team-formation/problem
*/


#include <stdio.h>
#include <time.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
const int N = 5e5+10;
ll tree[4*N];
int L[N],R[N],S[N],P[N];
vector<int> indices[N];
ll dp[N],dp2[N];
void update(int i, int j, int l, ll val, int ind)
{
 	if(l < i || l > j)
   		return;
   	if(i == j){
   		tree[ind] = val;
   		return;
   	}
   	int mid = (i+j)/2;
   	update(i,mid,l,val,2*ind);
   	update(mid+1,j,l,val,2*ind+1);
   	tree[ind] = max(tree[2*ind+1],tree[2*ind]);
}
ll query(int i, int j, int l, int r, int ind)
{
   	if(l > j || i > r)
   		return 0;
   	if(i >= l && j <= r)
   		return tree[ind];
   	int mid = (i+j)/2;
   	return max(query(i,mid,l,r,2*ind),query(mid+1,j,l,r,2*ind+1));
}
int main()
{
   	int n;
   	cin>>n;
   	for(int i = 1;i<=n;i++)
   		cin>>S[i];
   	for(int i = 1;i<=n;i++)
   		cin>>L[i];
   	for(int i = 1;i<=n;i++){
   		cin>>R[i];
   		if(i+R[i] < n)
   			indices[i+R[i]+1].emplace_back(i);
   	}
   	for(int i = 1;i<=n;i++)
   	{
   		for(int j:indices[i])
   			update(1,n,j,dp2[j],1);
   		int li = i-L[i]-1;
   		dp2[i] = (li<1?0:query(1,n,1,li,1))+S[i];
   		dp[i] = max(dp[i-1],dp2[i]);
   	}
   	cout<<dp[n];
}