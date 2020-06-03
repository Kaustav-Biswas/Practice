'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

For example, if s=abc , it is a valid string because frequencies are {a:1,b:1,c:1} . So is s=abcc because we can remove one c and have 1 of each character in the remaining string. If s=abccc however, the string is not valid as we can only remove 1 occurrence of c . That would leave character frequencies of {a:1,b:1,c:2}.

Function Description

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

s: a string
Input Format

A single string s.

Constraints

1<=|s|<=100000
Each character is a lower case alphabet.

Output Format

Print YES if string  is valid, otherwise, print NO.

Sample Input 0

aabbcd
Sample Output 0

NO
Explanation 0

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

Sample Input 1

aabbccddeefghi
Sample Output 1

NO
Explanation 1

Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove  characters with a frequency of : .
Remove  characters of frequency : .
Neither of these is an option.

Sample Input 2

abcdefghhgfedecba
Sample Output 2

YES
Explanation 2

All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.

'''



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    char_count = {i:s.count(i) for i in [chr(c) for c in range(97,123)]}
    new_dict = {i:j for i,j in char_count.items() if j>0}
    occur_count = {i:list(new_dict.values()).count(i) for i in list(new_dict.values())}
    if len(occur_count) == 1:
        return 'YES'
    elif len(occur_count) == 2 and 1 in occur_count.values():
        occ1, occ2 = [i[0] for i in sorted(occur_count.items(), key= lambda x:x[1])]
        if occ1 == 1 or occ1 == occ2+1:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
