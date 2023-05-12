#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s)//2+1):
        start = s[:i]
        exp = ""
        n = int(start)
        while len(exp) < len(s):
            exp += str(n)
            if exp == s:
                print("YES", start)
                return
            n += 1
    print("NO")
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
