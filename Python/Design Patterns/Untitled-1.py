#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    points_a = 0
    points_b = 0

    for i in range(0, len(a)-1):
        if a[i] > b[i]:
            points_a += 1 
        elif b[i] > a[i]:
            points_b +=1

    return(a, b)
        

if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    
    print(result)