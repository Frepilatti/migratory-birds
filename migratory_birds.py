#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    sorted_arr = sorted(arr, reverse=True)
    highest_count = 0
    highest_bird = 0
    count = 0
    bird = sorted_arr[0]
    
    for b in sorted_arr:
        if b == bird:
            count += 1
        else:
            if highest_count <= count:
                highest_count = count
                highest_bird = bird
            bird = b
            count = 0
    return highest_bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
