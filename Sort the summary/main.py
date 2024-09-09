#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the 'groupSort' function below.

# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.


def groupSort(arr):
    # Write your code here
    unique_digits = {}
    
    for number in arr:
        if unique_digits.get(number):
            unique_digits[number] += 1
        else:
            unique_digits[number] = 1
            
    group = [(k,v) for k, v in unique_digits.items()]
    
    group.sort(key=lambda x: (-x[1], x[0]))
    
    return group

if __name__ == '__main__':
    # Test cases
    print(groupSort([3, 3, 1, 2, 1])) # Expected [(1, 2), (3, 2), (2, 1)]
    print(groupSort([0,1,2,4,5,7])) # Expected [(0, 1), (1, 1), (2, 1), (4, 1), (5, 1), (7, 1)] 
