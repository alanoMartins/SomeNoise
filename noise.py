import numpy as np
import math
import cv2

variance = 1
mean = 0
X = range(-255, 255)

def gauss(x):
    expo = -0.5 * ((math.floor((x-mean) / variance)) ** 2)
    tmp = np.e ** expo
    tmp2 = (1 / (variance * (math.sqrt((2 * math.pi)))))
    return np.exp(expo) * (1 / (variance * (math.sqrt((2 * math.pi)))))

def calcFDA(vect):
    fdp = map(gauss, vect)
    fda = np.cumsum(fdp)
    return fda

def findNear(array, value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def applyNoise(pixel):
    amplitude = 0.1
    fda = calcFDA(X)
    noise = findNear(fda, np.random.random(1)[0]) * amplitude
    return pixel + noise

def calc():
    image = cv2.imread('/home/joker/Workspace/asserts/lena512.jpg', 0)
    for col in xrange(len(image)):
        for row in xrange(len(image[col])):
            image[col, row] = applyNoise(image[col, row])
            
    cv2.imshow('noise', image)
        
    
    

     

    
calc()