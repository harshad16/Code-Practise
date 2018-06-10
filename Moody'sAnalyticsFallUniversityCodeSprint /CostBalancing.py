"""
https://www.hackerrank.com/contests/moodys-analytics-fall-university-codesprint/challenges/cost-balancing/problem
You need to calculate the total expense.
Everybody should pay equal amount, which would be 
However, everybody have to pay a whole amount, so the everbody have to pay the integral part of the above fraction.
Anita decided to pay the rest of the money. Which is the remainder of the fraction, 
Finally, you have to calucalte how much money each person owes or gets.
To print the final answer you need to be careful about the output order. You may make use of map, vector and string
"""
#!/bin/python

import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    total=0
    given={}
    for a0 in xrange(n):
        id_number, amount = raw_input().strip().split(' ')
        id_number, amount = [int(id_number), int(amount)]
        if id_number in given:
            given[id_number]=given[id_number]+amount
        else:
            given[id_number]=amount
        total=total+amount
    share=total/m
    extra=total-share*m
    #print given
    for key,value in given.items():
        if key==1:
            print key,value-share-extra
        else:
            print key,value-share