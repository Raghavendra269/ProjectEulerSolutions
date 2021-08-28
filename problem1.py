'''
Find the sum of all the multiples of 3 or 5 below N.
'''


#!/bin/python3

import sys

def printsum(n):
    sum=0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            sum+=i
    print(sum)
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    printsum(n)
