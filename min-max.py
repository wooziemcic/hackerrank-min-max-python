import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_arr = []
    length = len(arr)
    for x in range(length):
        sum_arr.append(sum(arr)-arr[x])
    sum_arr.sort()
    print(sum_arr[0], sum_arr[-1])
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
