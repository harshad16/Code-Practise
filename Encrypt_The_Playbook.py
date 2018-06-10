# https://www.hackerearth.com/problem/algorithm/encrypt-the-playbook-6fff51d3-c063791b/description/
#  Encrypt "The Playbook"
# Barney needs to encrypt his "Playbook" so Lily won't be able to read the playbook, he has found a method to encrypt every single letter in the playbook but it is going to be very time consuming so he needs you to write a program to encrypt his "Playbook". He has provided the following instructions for encryption

# You have to use the english alphabets as in the keyboard of your pc Consider the 3 lines of input as Set 1, Set 2 and Set 3
# 1. For the first letter return the 3rd letter counting right from it's position from the same set( i.e. if first letter is in Set 1 return letter from the same.)
# 2. For the second letter return the 2nd letter counting left from it's position from the next set ( i.e. if second letter is in Set 1 return letter from the Set 2.)
# 3. For the third letter return the 1st letter counting left from it's position from the previous set( i.e. if third letter is in Set 1 return letter from the Set 3)
# 4. for the fourth letter return the letter in the same position from the next set( i.e. if fourth letter is in Set 1 return letter from the Set 2)
# repeat for the next letters considering the 5th as 1st and so on. If the string contains a letter more than once do not encrypt every occurence, in place of it put '.' at the end of the encrypted text.

# Input Format
# First line contains an integer n, number of test cases followed by test cases.

# Output Format
# Encrypted text for each test case in separate line.

# Its gonna be **legen** wait for it....
# SAMPLE INPUT 
# 1
# legen
# SAMPLE OUTPUT 
# dary.
# Explaination:
# For legen, letter 'e' is repeated, so only legn is considered and 1 dot (.) will be added at the end of the result
# 1. l is the first letter so 3rd letter counting right from it position is returned from same set i.e. 'd' 
# 2. e is the second letter so 2nd letter counting left from it position is returned from next set i.e. 'a' from Set 2
# 3. g is the third letter so 1st letter counting left from it position is returned from previous set i.e. 'r' from set 1 from 
# 4. n is the fourth letter so same positioned letter is returned from next set i.e. 'y' from set 1
# So legen got encrypted as dary. (with a dot at the end)
from collections import OrderedDict
set1=['q','w','e','r','t','y','u','i','o','p']
ns1=len(set1)
set2=['a','s','d','f','g','h','j','k','l']
ns2=len(set2)
set3=['z','x','c','v','b','n','m']
ns3=len(set3)
t=input()
for _ in range(t):
    q=raw_input()
    done=[]
    res=[]
    check={}
    n=''.join(OrderedDict.fromkeys(q))
    c=len(q)-len(n)
    for i,item in enumerate(n,start=1):
        if i%4==1:
            if item in set1:
                for e in range(0,ns1):
                    if item == set1[e]:
                        done.append(item)
                        if e+3>=ns1:
                            res.append(set1[(e+3)-ns1])
                            check[item]=set1[(e+3)-ns1]
                        else:
                            res.append(set1[e+3])
                            check[item]=set1[e+3]
            elif item in set2:
                for e in range(0,ns2):
                    if item==set2[e]:
                        done.append(item)
                        if e+3>=ns2:
                            res.append(set2[(e+3)-ns2])
                            check[item]=set2[(e+3)-ns2]
                        else:
                            res.append(set2[e+3])
                            check[item]=set2[e+3]
            else:
                for e in range(0,ns3):
                    if item == set3[e]:
                        done.append(item)
                        if e+3>=ns3:
                            res.append(set3[(e+3)-ns3])
                            check[item]=set3[(e+3)-ns3]
                        else:
                            res.append(set3[e+3])
                            check[item]=set3[e+3]

        elif i%4==2:
            if item in set1:
                for e in range(0,ns1):
                    if item == set1[e]:
                        done.append(item)
                        if e-2>=ns2:
                            res.append(set2[ns2-(e-2)])
                            check[item]=set2[ns2-(e-2)]
                        else:
                            res.append(set2[e-2])
                            check[item]=set2[e-2]
            elif item in set2:
                for e in range(0,ns2):
                    if item==set2[e]:
                        done.append(item)
                        if e-2>=ns3:
                            res.append(set3[ns3-(e-2)])
                            check[item]=set3[ns3-(e-2)]
                        else:
                            res.append(set3[e-2])
                            check[item]=set3[e-2]
            else:
                for e in range(0,ns3):
                    if item == set3[e]:
                        done.append(item)
                        if e-2>=ns1:
                            res.append(set1[ns1-(e-2)])
                            check[item]=set1[ns1-(e-2)]
                        else:
                            res.append(set1[e-2])
                            check[item]=set1[e-2]

        elif i%4==3:
            if item in set1:
                for e in range(0,ns1):
                    if item == set1[e]:
                        done.append(item)
                        if e-1>=ns3:
                            res.append(set3[(e-1)-ns3])
                            check[item]=set3[(e-1)-ns3]
                        else:
                            res.append(set3[e-1])
                            check[item]=set3[e-1]
            elif item in set2:
                for e in range(0,ns2):
                    if item==set2[e]:
                        done.append(item)
                        if e-1>=ns1:
                            res.append(set1[(e-1)-ns1])
                            check[item]=set1[(e-1)-ns1]
                        else:
                            res.append(set1[e-1])
                            check[item]=set1[e-1]
            else:
                for e in range(0,ns3):
                    if item == set3[e]:
                        done.append(item)
                        if e-1>=ns2:
                            res.append(set2[(e-1)-ns2])
                            check[item]=set2[(e-1)-ns2]
                        else:
                            res.append(set2[e-1])
                            check[item]=set2[e-1]

        elif i%4==0:
            if item in set1:
                for e in range(0,ns1):
                    if item == set1[e]:
                        done.append(item)
                        if e>=ns2:
                            res.append(set2[(e)-ns2])
                            check[item]=set2[(e)-ns2]
                        else:
                            res.append(set2[e])
                            check[item]=set2[e]
            elif item in set2:
                for e in range(0,ns2):
                    if item==set2[e]:
                        done.append(item)
                        if e>=ns3:
                            res.append(set3[(e)-ns3])
                            check[item]=set3[(e)-ns3]
                        else:
                            res.append(set3[e])
                            check[item]=set3[e]
            else:
                for e in range(0,ns3):
                    if item == set3[e]:
                        done.append(item)
                        if e>=ns1:
                            res.append(set1[(e)-ns1])
                            check[item]=set1[(e)-ns1]
                        else:
                            res.append(set1[e])
                            check[item]=set1[e]

    if c>0:
        for _ in range(c):
            res.append('.')
        print ''.join(res)
    else:
        print ''.join(res)