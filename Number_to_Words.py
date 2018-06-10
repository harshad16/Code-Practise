# https://www.hackerrank.com/contests/projecteuler/challenges/euler017/copy-from/1303789961
# The numbers 1 to 5 written out in words are One,Two,Three,Four,Five
# First character of each word will be capital letter for example: 
# 1234567890 is One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety
# Given a number, you have to write it in words.

# Input Format
# The first line contains an integer t, i.e.,t number of test cases. 
# Next t lines will contain an integer n.

# Constraints
# 1<=T<=10
# 0<=n<=10^12
# Output Format
# Print the values corresponding to each test case.

import re
word_map={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
         11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",
         18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",
         80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand",1000000:"Million",
         1000000000:"Billion",1000000000000:"Trillion"}

def tens(x,y,val):
    if y in word_map:
        val=val+word_map[y]
        y=y%10
    else:
        x=(x/10)*10
        y=y%(10)
        val=val+word_map[x]+word_map[y]
    return x,y,val

def huns(x,y,val):
    val=val+word_map[x/100]+word_map[100]
    x=x%(10**2)
    y=y%(10**2)            
    return x,y,val

t=input()
for _ in range(t):
    n=input()
    val=""
    if n==0:
        print "Zero"
    elif n in word_map:
        print word_map[n]
    else:
        l=len(str(n))
        x=n
        y=n
        while(len(str(y))!=1):
            if len(str(y))==2:
                x,y,val=tens(x,y,val)
            elif len(str(y))==3:
                x,y,val=huns(x,y,val)
            elif len(str(y))==4:
                val=val+word_map[x/1000]+word_map[1000]
                x=x%(10**3)
                y=y%(10**3)
            elif len(str(y))==5:
                x1,y1,val1=tens(x/1000,x/1000,"")
                val=val+val1+word_map[1000]
                x=x%(10**3)
                y=y%(10**3)
            elif len(str(y))==6:
                x1,y1,val1=huns(x/1000,x/1000,"")
                x2,y2,val1=tens(x1,y1,val1)
                val=val+val1+word_map[1000]
                x=x%(10**3)
                y=y%(10**3)
            elif len(str(y))==7:
                val=val+word_map[x/1000000]+word_map[1000000]
                x=x%(10**6)
                y=y%(10**6)    
            elif len(str(y))==8:
                x1,y1,val1=tens(x/1000000,x/1000000,"")
                val=val+val1+word_map[1000000]
                x=x%(10**6)
                y=y%(10**6)
            elif len(str(y))==9:
                x1,y1,val1=huns(x/1000000,x/1000000,"")
                x2,y2,val1=tens(x1,y1,val1)
                val=val+val1+word_map[1000000]
                x=x%(10**6)
                y=y%(10**6)
            elif len(str(y))==10:
                val=val+word_map[x/1000000000]+word_map[1000000000]
                x=x%(10**9)
                y=y%(10**9)    
            elif len(str(y))==11:
                x1,y1,val1=tens(x/1000000000,x/1000000000,"")
                val=val+val1+word_map[1000000000]
                x=x%(10**9)
                y=y%(10**9)
            elif len(str(y))==12:
                x1,y1,val1=huns(x/1000000000,x/1000000000,"")
                x2,y2,val1=tens(x1,y1,val1)
                val=val+val1+word_map[1000000000]
                x=x%(10**9)
                y=y%(10**9)
            elif len(str(y))==13:
                val=val+word_map[x/(10**12)]+word_map[(10**12)]
                x=x%(10**12)
                y=y%(10**12)
        
        if str(n)[-2]=="0" and str(n)[-1]!="0":
            val=val+word_map[y]
        print re.sub(r"(?<=\w)([A-Z])", r" \1", val)    
        