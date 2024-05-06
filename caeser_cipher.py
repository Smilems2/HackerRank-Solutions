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
    m=""
    if k>26:
        while (k>26):
            k-=26
    Write your code here
    for i in s:
        if i.isalpha():
            if i.islower():
                if (ord(i)<=(122-k)):
                    m+=chr(ord(i)+k)
   
                else:
                    m+=chr(ord(i)-26+k)
            if i.isupper():
                if (ord(i)<=(90-k)):
                    m+=chr(ord(i)+k)
   
                else:
                    m+=chr(ord(i)-26+k)
        else:
            m+=i
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
