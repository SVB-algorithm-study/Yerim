#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    noNumber = 1
    noLower = 1
    noUpper = 1
    noSpecial = 1
    
    for p in password:
        if p in numbers:
            noNumber = 0
        elif p in lower_case:
            noLower = 0
        elif p in upper_case:
            noUpper = 0
        elif p in special_characters:
            noSpecial = 0
            
    lack = noNumber + noLower + noUpper + noSpecial
    
    return lack if lack > 6-n else 6-n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
