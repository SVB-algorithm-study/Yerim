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

def separateNumbers(s): # Not sure. O(n^3)
    # Write your code here
    if len(s) == 1:
        print("NO")
        return
    
    def check(ed, n):
        l = len(str(n+1))
        if ed+l > len(s):
            return False
        slc = s[ed:ed+l]
        if slc[0] != '0' and int(slc) == n+1:
            if ed+l == len(s):  
                return True
            else:
                return check(ed+l, n+1)
        else:
            return False
            
    for i in range(1, len(s)//2+1):
        fst = s[:i]
        if check(i, int(fst)):
            print("YES " + fst)
            return
    print("NO")
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
