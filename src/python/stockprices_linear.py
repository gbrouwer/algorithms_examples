import os
import sys
import numpy as np 

#-----------------------------------------------------------
if __name__ == '__main__':

    #Input
    prices = [100, 180, 260, 310, 40, 535, 695]

    #Double loop
    absMin = prices[0]
    buydate = -1
    selldate = -1
    maxprofit = -1
    for i in range(len(prices)):
        curVal = prices[i]
        if (curVal < absMin):
            absMin = curVal
            buydate = i
        diff = curVal - absMin
        if (diff > maxprofit):
            maxprofit = diff
            selldate = i

    print(buydate,selldate,maxprofit)
