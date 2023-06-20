#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import Counter 

def anagram(s):
    # Write your code here
    l = len(s)
    if l%2 == 1:
        return -1
    
    s1 = s[:l//2]
    s2count = Counter(s[l//2:])
    
    ans = 0
    for i in s1:
        if s2count.get(i, 0) == 0:
            ans += 1
        else:
            s2count[i] -= 1
    return ans 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
