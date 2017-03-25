import numpy as np
import math
import cv2
import noises as no

variance = 1
mean = 0
X = np.linspace(0,1,10)
img = []

def calcFDA(vect, func):
    fdp = []
    for item in range(0, len(vect)):
        fdp.append(func(vect[item]))
    fda = np.cumsum(fdp)
    return fda

def findNear(array, value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def applyNoise(pixel, fda):
    amplitude = cv2.getTrackbarPos('amplitude','image')
    noise = findNear(fda, np.random.random(1)[0]) * amplitude * 10
    return pixel + noise


def nothing(x):
    pass

def calc(fda):
    img = cv2.imread('/home/atlanticolab/Imagens/lena512.bmp', 0)
    for col in xrange(len(img)):
        for row in xrange(len(img[col])):
            img[col, row] = applyNoise(img[col, row], fda)
            
    cv2.imshow('image',img)
    
def calcGauss(vect):
    fda = calcFDA(vect, no.gauss)
    calc(fda)
    
def calcErlang(vect):
    fda = calcFDA(vect, no.erlang)
    calc(fda)
    
def calcExponencial(vect):
    fda = calcFDA(vect, no.exponencial)
    calc(fda)
    
def calcPoisson(vect):
    fda = calcFDA(vect, no.poisson)
    calc(fda)
    
def calcRayleigh(vect):
    fda = calcFDA(vect, no.rayleigh)
    calc(fda)
    
def calcUniforme(vect):
    fda = calcFDA(vect, no.uniforme)
    calc(fda)    
    
       

def init():
    
    cv2.namedWindow('image')
    
    cv2.createTrackbar('variance','image',1,300,nothing)
    cv2.createTrackbar('mean','image',1,10,nothing)
    cv2.createTrackbar('amplitude','image',1,100,nothing)
    
    while(1):
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            exit() 
        if k == ord('g'):
            calcGauss(X)
        if k == ord('l'):
            calcErlang(X)        
        if k == ord('e'):
            calcExponencial(X)
        if k == ord('p'):
            calcPoisson(X) 
        if k == ord('r'):
            calcRayleigh(X)
        if k == ord('u'):
            calcUniforme(X)            
init()