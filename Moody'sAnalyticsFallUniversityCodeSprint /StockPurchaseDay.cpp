/*
https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/stock-purchase-day/editorial
Let suffmn[i] denotes the minimum stock price from the ith day to the nth day and cost[i] denotes the cost of stock in ith day.
Base Case:
suffmn[n] = cost[n]
Recurrence:
suffmn[i] = minimum(suffmn[i + 1] , cost[i]) 
After constructing this suffix minimum array, for each customer willing to buy the product for value x, we will do binary search on this suffix minimum array to find the largest index idx, such that suffmn[idx] is less than or equal to the value x.
Binary search works because suffix minimum array is always in non-decreasing order because suffmn[i] <= suffmn[j] for all i <= j. Since, for i <= j, minimum stock price from day i to day n, also takes minimum of all the stock prices from day j to day n.
Binary Search:
We compare middle value of suffmn array with the value x, and if:
x is greater or equal to suffmn[mid] then we go to the right half and not left half because x will always be greater or equal to all the values on its left half, so we will move towards right half and find the largest day number where stock can be purchased.
x is less than suffmn[mid] then we go to the left half and not right half because we will not be able to purchase stock in right half since x will always be less than all the values on its right half, so we will move towards left half, and find the largest day number where stock can be purchased.
Binary Search Code Snippet:
int mx = -1; // stores the last day where stock can be purchased with value x
int lo = 1; // lower limit of binary search
int hi = n; // upper limit of binary search
while(lo <= hi) {
    int mid = (lo + hi) / 2;
    if(x >= suffmn[mid]) {
        mx = max(mx , mid);
        lo = mid + 1;
    } else {
        hi = mid - 1;
    }
}
If the value of mx is -1, then the purchase is impossible, else mx is the last day where the person can buy stock with value x.
*/

# include "bits/stdc++.h"
using namespace std;
const int N = 1e5 + 5;
int n;
int arr[N];
int suffmn[N];
int q;
int x;

int solve(int x) {
	int mx = -1;
	int lo = 1;
	int hi = n;
	while(lo <= hi) {
		int mid = (lo + hi) / 2;
		if(suffmn[mid] <= x) {
			mx = max(mx , mid);
			lo = mid + 1;
		} else {
			hi = mid - 1;
		}
	} 
	return mx;
}

int main() {
	scanf("%d" , &n);
	for(int i = 1; i <= n; ++i) {
		scanf("%d" , arr + i);
	}
	suffmn[n] = arr[n];
	for(int i = n - 1; i >= 1; --i) {
		suffmn[i] = min(suffmn[i + 1] , arr[i]);
	}
	scanf("%d" , &q);
	while(q--) {
		scanf("%d" , &x);
		printf("%d\n" , solve(x));
	}
	return 0;
}