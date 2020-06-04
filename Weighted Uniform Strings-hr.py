'''
A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are 1 to 26 from a to z as shown below:We define the following terms:
The weight of a string is the sum of the weights of all the string's characters. For example:
apple = 1+16+16+12+5=50
A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.
Given a string, s, let U be the set of weights for all possible uniform contiguous substrings of string s. You have to answer n queries, where each query i consists of a single integer, x[i]. For each query, print Yes on a new line if x[i] is an element of U; otherwise, print No instead.

Function Description

Complete the weightedUniformStrings function in the editor below. It should return an array of strings, either Yes or No, one for each query.
weightedUniformStrings has the following parameter(s):

s: a string
queries: an array of integers

Input Format

The first line contains a string s, the original string.
The second line contains an integer n, the number of queries.
Each of the next n lines contains an integer x[i], the weight of a uniform subtring of s that may or may not exist.

Constraints
1<= |s|,n <=100000
1<=x[i]<=10000000
s will only contain lowercase English letters, ascii[a-z].

Output Format
Print n lines. For each query, print Yes on a new line if x[i] is an element of U. Otherwise, print No.

'''


import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    res = []
    rev_wt = { j:chr(96+j) for j in range(1,27)}
    for n in queries:
        flag = 1
        factors = list(filter(lambda x: n%x==0, rev_wt))
        for i in factors:
            substring = rev_wt[i]*(n//i)
            if re.search(substring, s):
                res.append('Yes')
                flag = 0
                break
        if flag :
            res.append('No')
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
