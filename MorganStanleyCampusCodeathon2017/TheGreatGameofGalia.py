"""
https://www.hackerrank.com/contests/morgan-stanley-codeathon-2017/challenges/the-great-game-of-galia
First, we sort all the numbers in the array. Now a number can be in the leaf node in Binary Search Tree if it is inserted later than the two neighboring numbers.
So, from all 6 permutations of these three numbers, this number comes last in two permutations. 
So, the probability of being a leaf node for a number is 1/3 except for first and the last numbers(they have just one neighbor). 
So, their probability of being leaf node is 1/2. So expected sum is A[0]/2 + A[1]/3 + A[2]/3 + ... + A[n-3]/3 + A[n-2]/3 + A[n-1]/2.
"""
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def expectedAmount(a):
    # Complete this function
    a=sorted(a)
    fi=a[0]+a[-1]
    la=sum(a[1:-1])
    p=3*fi+2*la
    q=6
    if q/gcd(p,q)==1:
        print p/6
    else:
        print str(p/gcd(p,q))+"/"+str(q/gcd(p,q))
    

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        a = map(int, raw_input().strip().split(' '))
        expectedAmount(a)
