"""
https://www.hackerrank.com/contests/morgan-stanley-codeathon-2017/challenges/millionaire-finally
"""
n,m,k=map(int,raw_input().split(" "))
a=map(int,raw_input().split(" "))
b=map(int,raw_input().split(" "))
c=[]

for i in range(n):
    c.append(b[i]*m*a[i])

if max(c)>k*m:
    print max(c)
else:
    print k*mx