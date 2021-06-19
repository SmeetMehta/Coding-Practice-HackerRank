import math
import os
import random
import re
import sys

def timeConversion(s):
    x=s[len(s)-2:]
    y=int(s[:2])
    if x == 'AM':
         if y==12:
            return '00'+s[2:len(s)-2]
        else:
            return s[:len(s)-2]
    else:
        if y==12:
            return s[:len(s)-2]
        else:
            return str(y+12)+s[2:len(s)-2]
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
