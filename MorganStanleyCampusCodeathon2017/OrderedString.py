"""
# https://www.hackerrank.com/contests/morgan-stanley-codeathon-2017/challenges/shell-sort-command/problem

This problem is a variation of a Unix sort command, and in order to solve it one has to implement a subset of functionalities available in the original command.
There are  strings given in the input, and each of them contains the same number of columns consisting of numeric characters only.
These columns are separated by spaces. For example, a string 123 022 22 contains 3 columns.
In addition to that, you are given 3 parameters:
key: integer denoting the column used as a key in comparisons. The left-most column is denoted by 1.
reversed: boolean variable indicating whether to reverse the result of comparisons
comparison-type: either lexicographic or numeric. Lexicographic means that we use Lexicographical order where for example 122<13. 
Numeric means that we compare the strings by their numerical values, so 13<122.If the comparison type is numeric and numeric values of keys of si and sj are equal for i<j, 
then si is considered strictly smaller than sj because it comes first.
The goal is to sort all n inputs strings according to values of the above parameters and print the strings in the resulting order.
Let's examine the parameters one by one.
key: denotes just a column used while comparing the strings, and it takes values from 1 to the number of columns in the strings (as stated before, 
all strings have the same number of columns). Thus if we have a string 123 022 22 and key is 2, then we use 022 in all comparisons involving this string.
reversed: is very sstraightforward to handle. Let's assume that we have two string si and sj, and we want to compare them.
Moreover, let's assume that si compares less than sj, then if reversed is false, we return that indeed si compares less than sj. 
Otherwise, is reversed is true, we return that si compares less than sj.
comparison-type: this parameter can possibly cause the most problems. It can take either one of values lexicographical or numeric.
It's important to handle both well. lexicographical means that we compare keys of given string using their string values, so 122 < 13. 
Notice that in case of lexicographical comparison there are no draws because all column values are guaranteed to be unique.
In the other case, when comparison-type is numeric, we compare keys of given string using their numerical (integer in this case) values. 
Thus 13 < 122. Just be aware that there is one tricky case to handle. Let's assume that we're comparing keys of strings si and sj,
and at least one of the compared keys begins with . In this case, it's possible that both keys have equal numerical values.
For example, keys 022 and 22 have the same numerical values. Whenever this happens, according to the rules given in the statement,si<sj  if and only if i<j.
This assures that there are no draws, so the resulting order is unique for any input.
The above method can be implemented in O(n.log(n)) time. Moreover, it's far more efficient to sort only the keys rather than whole strings,
and then use the sorted keys to produce the output. For details of such implementation, please refer to my code below.
"""

n = int(raw_input())

ss = []
for _ in xrange(n):
    s = raw_input()
    ss.append(s.split())

col, rev, ctype = raw_input().split()
col = int(col)-1

rev = True if rev == "true" else False

tmp = []
for i in xrange(n):
    tmp.append((int(ss[i][col]) if ctype == "numeric" else ss[i][col], i))

for _, idx in sorted(tmp, reverse=rev):
    print " ".join(map(str, ss[idx]))