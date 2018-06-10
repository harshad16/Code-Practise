/*
https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/modified-subsequence-sum/problem
First we note we can come up with a dynamic programming solution. To do this we let  denote the maximum value of  for all subsequences with the rightmost term of . Then we see . However if we try to implement this by checking all  we will get a solution of , which is too slow for the limits given.
To speed up the solution we look at the term  for a given . We can rewrite this as . Next we note to find the maximum value attained by this term we can find the maximum value attained by  over all  and add to the answer since  does not depend on .
Finally to find the maximum value attained by  over all  we let . Thus we see our problem is to find the . It turns out since the  are linear functions this problem can be solved using the Convex Hull Trick.
Furthermore due to the fact that if  then  has a larger gradient than  the sorting step usually required in the Convex Hull trick is not required. Also because we evaluate the values of  at increasing points we can use a pointer walk instead of a binary search. These two results mean that the solution using the Convex Hull Trick becomes  instead of O(nlogn).
*/

#include <bits/stdc++.h>

using namespace std;

//Convex Hull trick implementation

class CHT{
public:
  vector<pair<long long, long long>> lines;
  int pos;
  CHT():pos(0){}
  
  //adding lines to the hull

  bool isBad(int l1, int l2, int l3){
    long long m1=lines[l1].first, m2=lines[l2].first, m3=lines[l3].first;
    long long c1=lines[l1].second, c2=lines[l2].second, c3=lines[l3].second;
    return (__int128)(c1-c3)*(m2-m1)<(__int128)(c1-c2)*(m3-m1);
  }
  void add(long long m, long long c){
    lines.push_back(make_pair(m,c));
    
    int lsz=lines.size();
    while(lsz>=3 && isBad(lsz-3,lsz-2,lsz-1)){
      lines.erase(lines.end()-2);
      lsz=lines.size();
    }
    

  }
  
  //using a pointer walk to find the line that gives the largest value at a point
  long long query(long long x){
    int lsz=lines.size();

    
    if(pos>=lsz)
      pos=lsz-1;
    while(pos<lsz-1 && lines[pos].first*x+lines[pos].second<lines[pos+1].first*x
	  +lines[pos+1].second){
      pos++;
    } 
    
    return lines[pos].first*x+lines[pos].second;
  }

  
};

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    long long k;
    cin>>n>>k;
    vector<long long> a(n);
    for(int i=0; i<n; i++){
      cin>>a[i];
    }

    CHT cht;

    vector<long long> dp=a;   
    cht.add(2*k,-k+a[0]);
    for(int i=1; i<n; i++){     
      
      dp[i]=max(dp[i],cht.query(i)+a[i]-k*i*i);
      cht.add(2ll*k*(i+1),-k*(i+1)*(i+1)+dp[i]);

      
		
    }

    cout<<*max_element(dp.begin(),dp.end()); 
    
    return 0;
}