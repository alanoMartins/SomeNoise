import cv2
import math
import numpy as np

def gauss(x):
    mean = cv2.getTrackbarPos('mean','image')
    variance = cv2.getTrackbarPos('variance','image') + 1
    
    expo = -0.5 * ((math.floor((x-mean) / variance)) ** 2)
    tmp = np.e ** expo
    tmp2 = (1 / (variance * (math.sqrt((2 * math.pi)))))
    return np.exp(expo) * (1 / (variance * (math.sqrt((2 * math.pi)))))

def uniforme(x):
    a = 10
    b = 20
    if x >= a and x <= b :
        1 / (b - a)
    else:
        0
        
def erlangIn(x, a, b):
    
    if x < 0:
        return 0
    else:
        expo = np.exp(-a * x)
        divz = (a ** b) * (x ** (b - 1))
        divd = np.math.factorial((b-1))
        return (divz / divd) * expo
    
def erlang(x):
    a = 10
    b = 10
    
    return erlangIn(x, a, b) 

def exponencial(x):
    a = cv2.getTrackbarPos('mean','image') * 100
    b = 1
    
    return erlangIn(x, a, b)

def poisson(x): 
    if x < 0:
        return 0
    else:
        mean = cv2.getTrackbarPos('mean','image')
        return (np.exp(-mean) * (mean ** x)) / np.math.factorial(x)

def rayleigh(x):
    a = cv2.getTrackbarPos('mean','image')
    b = cv2.getTrackbarPos('variance','image')
    
    if x < a:
        return 0
    else:
        expo = np.exp(- (((x - a) ** 2) / b))
        return (2 / b) * (x - a) * expo