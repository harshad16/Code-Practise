dp={}
def is_prime(a):
    return all(a%i for i in xrange(2,(a/2+1)))

def fact(a):
    if a in dp:
        return dp[a]
    elif a==0:
        dp[a]=1
        return 1
    else:
        f=a*fact(a-1)
        dp[a]=f
        return f

val=1000000007
t=input()
for j in range(t):
    n,m=map(int,raw_input().split(" "))
    v=map(int,raw_input().split(" "))
    if max(v)==m:
        print 1
    else:
        i=max(v)
        t=[item for item in range(i,m+1) if not is_prime(item)]
        v1=fact(len(t))/fact(len(t)-n)
        v2=[item for item in v if item!=i and not is_prime(item)]
        v3=fact(len(t))/fact(len(t)-n-1)
        print (v1+v3*len(v2))%val
            