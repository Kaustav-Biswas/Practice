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
