import os
import sys
import numpy as np 

#-----------------------------------------------------------
if __name__ == '__main__':

    #Input
    prices = [100, 180, 260, 310, 40, 535, 695]

    #Double loop
    maxDiff = 0
    buy = 0
    sell = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            diff = np.abs(prices[i] - prices[j])
            if (diff > maxDiff and i < j):
                maxDiff = diff
                buy = i
                sell = j

    print(buy,sell,maxDiff)
