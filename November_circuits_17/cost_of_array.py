"""
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/approximate/cost-of-array-aea53591/

Given two length-n arrays a and b, we define the score by the dot product between them, i.e., ∑ ni=ai∗bi. The original score is denoted as S
You can apply at most 2^20 swaps to modify the array a. The cost of swaping ax and ay is cost [ax][ay]. The total cost is denoted as C.
After your swaps, we can recompute the score again, denoted as S′. The final score is max(0, S′−S−C). You want to maximize this score.
Input 
The first line contains one number n(1≤n≤2^18).
The second line contains n numbers-a1,a2,a3,…,an (0≤ai<m).
The third line contains n numbers -b1,b2,b3,…,bn (0≤ bi< 2^30).
The fourth line contains one number m (1≤m≤512).
The next m lines contains m integers representing the matrixcost[i][j] (0≤cost[i][j] < 230, cost[i][i]=0, cost[i][j]=cost[j][i]).
Output
The first line contains one numberkk(0≤k≤2^20) - the number of swaps.
The next k lines contains two numbers separated by space ui,vi - signifying that at step i you will swap values a_{u_{i}},a_{v_{i}}
Scoring
The final score is max(0, S′−S−C).You want to maximize this score.
Tests
The will be in total 100 with 4 types of generation:
1. m=512
2. m=512 and 70% of values in matrixcost  are smaller than 2^10
3. m=64 
4. m=512 and 0≤bi<2^10(1≤i≤n).
SAMPLE INPUT
3
2 1 0
1 2 3
3
0 1 1
1 0 1
1 1 0
SAMPLE OUTPUT
1
1 3
Explanation
You swap indices 1 and 3 with cost 1 and obtain the final sequence[0, 1, 2]. The final score score is max(0, 8−4−1) = 3.
"""
