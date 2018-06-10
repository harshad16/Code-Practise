/*
https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/lets-play-a-game-2/problem

You can see that the given sequence of moves forms a complete bipartite graph. Hence the problem reduces to finding LIS on a complete bipartite graph.
Consider the following statement :
For a complete bipartite graph Km,n where set A of vertices has m vertices and set B of vertices has n vertices and m>=n, there exists an LIS that contains all the vertices of set B.
The proof of the above lemma can be read from link.
Now we know that we need to add each vertex of set B in the LIS. Hence, for each adjacent element of set B, add an element from set A that has its value between the given two elements of set B.
*/

#include <bits/stdc++.h>
using namespace std;

vector<int> wx, wy;
int main() {
 	int n, i, j, ans = 0, m;
 	string s;
 	scanf("%d", &n);
 	cin>>s;
 	for(i = 0; i < n; i++) {
    	scanf("%d", &j);
    	if(s[i] == 'R' || s[i] == 'B')
    		wx.push_back(j);
    	else
    		wy.push_back(j);
    }

	n=wx.size(); m=wy.size();
	sort(wx.begin(), wx.end()); sort(wy.begin(), wy.end());
	if(n < m) {
		swap(wx, wy);
    	swap(n, m);
    }
  	if(m == 0) {
  		cout << 1 << endl;
    	return 0;
    }
  	ans = m;
  	j = 0;
  	if(n > m) {
    	if(wx[0] < wy[0])
    		ans++, j++;
    	if(wx[n-1] > wy[m-1])
    		ans++;
    }
	else if(wx[0] < wy[0])
		ans++, j++;
	else if(wx[n-1] > wy[m-1])
		ans++;

	for(i = 0; i < m-1; i++) {
    	while(j < n && wx[j] < wy[i])
			j++;
    	if(j < n && wx[j] > wy[i] && wx[j] < wy[i+1])
			ans++;
    }
	printf("%d\n", ans);
	return 0;
}