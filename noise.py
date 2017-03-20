import numpy as np
import math
import cv2
import noises as no

variance = 1
mean = 0
X = range(-255, 255)

def calcFDA(vect):
    fdp = []
    for item in range(0, len(vect)):
        fdp.append(no.exponencial(item))
    fda = np.cumsum(fdp)
    return fda

def findNear(array, value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def applyNoise(pixel, fda):
    amplitude = cv2.getTrackbarPos('amplitude','image')
    noise = findNear(fda, np.random.random(1)[0]) * amplitude
    return pixel + noise


def nothing(x):
    pass

def calc():

    img = cv2.imread('/home/atlanticolab/Imagens/lena512.bmp', 0)
    cv2.namedWindow('image')
    
    cv2.createTrackbar('mean','image',1,100,nothing)
    cv2.createTrackbar('variance','image',1,100,nothing)
    cv2.createTrackbar('amplitude','image',1,100,nothing)
    
    
    while(1):
        
        fda = calcFDA(X)
        for col in xrange(len(img)):
            for row in xrange(len(img[col])):
                img[col, row] = applyNoise(img[col, row], fda)
                
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break            
    
    cv2.destroyAllWindows()
    
calc()    