#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    answer = ''
    for i in s:
        if i.isalpha():
            k %= 26
            rot = ord(i) + k # ord() : unicode decimal숫자 반환
            (min, max) = (65, 90) if i.isupper() else (97, 122)
            i = chr(rot) if (min <= rot and rot <= max) else chr(rot - 26) # chr() : 다시 unicode로.
            # min 값은 굳이 필요하지 않다! 0<=k 이기 때문에 max값만 있어도 충분함.
        answer += i
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()