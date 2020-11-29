import  os
import sys
import numpy as np 

#--------------------------------------------------------
if __name__ == '__main__':

    #Coins
    monUnits = [1,5,10,25,100][::-1]
    monNames = ['penny','nickel','dime','quarter','dollar'][::-1]
    monUnits = np.array(monUnits)

    #Item cost and amount paid
    itemcost = int(1.30 * 100)
    paid = int(10.00 * 100)
    changeamount = paid - itemcost
cl    change = {}

    for m,monUnit in enumerate(monUnits):
        if (monUnit <= changeamount):
            nCoins = changeamount // monUnit
            change[monNames[m]] = nCoins
            changeamount = changeamount - (nCoins*monUnit)

    print(change)