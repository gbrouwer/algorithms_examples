import numpy as np
import os
import sys

#--------------------------------------------
if __name__ == '__main__':

	#Dice 1
	weights1 = np.array([1,1,1,1,1,2]).astype('float')
	probability1 = weights1 / np.sum(weights1)

	#Dice 2
	weights2 = np.array([2,1,1,1,1,1]).astype('float')
	probability2 = weights2 / np.sum(weights2)

	#Co occurence matrix
	matrix = np.zeros((6,6))
	for i,prob1 in enumerate(probability1):
		for j,prob2 in enumerate(probability2):
			matrix[i,j] = prob1 * prob2
	
	#Normalize	
	matrixNorm = matrix / np.sum(matrix)
	
	#Get all pairs
	sumValueDic = {}
	countValueDic = {}
	for i in range(6):
		for j in range(6):
			sumvalue = i+1 + j+1
			if sumvalue in sumValueDic:
				curProb = sumValueDic[sumvalue]
				sumValueDic[sumvalue] = curProb + matrixNorm[i,j]
				countValueDic[sumvalue] = countValueDic[sumvalue] + 1
			else:
				sumValueDic[sumvalue] = matrixNorm[i,j]
				countValueDic[sumvalue] = 1

	probValueDic = {}
	totalProb = 0
	for i in range(1,12):
		prob = sumValueDic[i+1]
		count = countValueDic[i+1]
		probValueDic[i+1] = prob / count
		totalProb = totalProb + prob

	for i in range(1,12):
		prob = probValueDic[i+1]
		probNorm = prob / totalProb
		print(i,probNorm)
