#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:01:42 2018

@author: MattFong
"""

#input x, y, eps1, eps2, R' or X'

def convertIntoTangentialShear(x, y, e1, e2):
    #...
    return r, g_tan, eMagnitude


def binDat(data, r, weight, X):
    #withScaling data = g_tan/scalingFactor, X = R'/r_s
        #stackDat = <F(x)>, stackX = <X>, errStack = sig_{<F(x)>}
    #withoutScaling data = g_tan, X = X'
        #stackDat = <deltaSigma(x)>, stackX = <R>, errStack = sig_{<deltaSigma(R)>}
    
    return stackDat, stackX, errStack


def woScalingInd(r, gtan, eMagnitude, presetR):
    #Calculate weight
    deltaSigma, R, errSigma = binDat(gtan, r, weight, presetR)
    
    return deltaSigma, R, errSigma
    

def wScalingInd(r, gtan, eMagnitude, presetX):
    #calculate weight
    #bin for fit and fit 
    #get scaling factor
    #f = g/scalingFactor
    F, X, errF = binDat(f, r, weight, presetX)
    return F, X, errF

#inputs: directoryName, fileNames (of clusters), method, 
#preset X or R

#directoryName = directory with individual cluster catalog files
#fileNames = list of individual cluster catalog file names
#method either 'wScaling' or 'woScaling'
#presetX =  X [] or R [Mpc], depending on method

#Below is an example of 'woScaling' method
def stack(directoryName, fileNames, method, presetX):
    
    stackDat = [0]*len(presetX)
    err = [0]*len(presetX)
    avgRad = [0]*len(presetX)
    
    
    for fileName in fileNames:
        grid = #import data from file name gridName
        x = grid[0,:]
        y = grid[1,:]
        e1 = grid[2,:]
        e2 = grid[3,:]
        
        r, g, eMag = convertIntoTangentialShear(x, y, e1, e2)
        
        indStackDat = []
        indR = []
        indErr = []
        if method == 'woScaling':
            #woScaling:
            indStackDat, indR, indErr = woScalingInd(r, g, eMag, \
                                                            presetX)
        
        if method == 'wScaling':
            indStackDat, indR, indErr = wScalingInd(r, g, eMag, presetX)
        
        
        #stackingProcess uses wScaling or woScaling outputs 
        #and adds into stack with preset R' or X'
        #Calculate stacks
        for i in len(R):
            stackDat[i] = stackDat[i]+indStackDat[i]
            #same for indR, indErr
            
        return stackDat, err, avgRad


