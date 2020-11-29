import numpy as np 
import pandas as pd 
import os 
import sys
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.spatial.distance import cdist
from tqdm import tqdm

#----------------------------------------------------------------
def createFakeData(nRows,nClusters,noiselevel,nDim):
    
    #Create Centroid for clusters
    y = []
    X = np.zeros((nRows*nClusters,nDim))
    xval = np.sin(np.linspace(0,2*np.pi,nClusters+1))[:nClusters]
    yval = np.cos(np.linspace(0,2*np.pi,nClusters+1))[:nClusters]

    #Create Data
    for i in range(nClusters):
        offset = i*nRows
        S = np.eye(2)
        x = np.random.multivariate_normal([xval[i],yval[i]],S*noiselevel,nRows)
        X[offset:offset+nRows,0] = x[:,0]
        X[offset:offset+nRows,1] = x[:,1]
        y = y + (np.zeros((nRows))+i).tolist()

    #Visualize Data
    plt.figure(figsize=(12,12))
    plt.scatter(X[:,0],X[:,1])
    plt.savefig('kmeans1.png')

    #Return
    return X,y

#----------------------------------------------------------------
def kmeans(X,y,k,tolerance,stepsize):

    #Init
    means = np.random.random((k,X.shape[1])) - 0.5
    clusters = np.zeros((len(y)))

    #EM step 1: Assign Member Ship
    D = cdist(X,means)
    print(D.shape)

    #Return clusters
    return clusters

#----------------------------------------------------------------
if __name__ == '__main__':

    #Create Fake Data
    nRowsPerCluster = 50
    nClusters = 6
    noiselevel = 0.025
    nDim = 2
    X,y = createFakeData(nRowsPerCluster,nClusters,noiselevel,nDim)

    #K-means
    k = 6
    tolerance = 0.0001
    stepsize = 0.01
    clusters = kmeans(X,y,k,tolerance,stepsize)

    #Draw Final Figure
    print(clusters)