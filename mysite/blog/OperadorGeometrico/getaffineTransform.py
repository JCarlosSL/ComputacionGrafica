import numpy as np
import cv2 as cv

def getaffineTransform(src,dst):
    A = np.zeros((6,6))
    b = np.zeros(6)
    X = np.zeros((6))
    M = np.zeros((2,3))

    for i in range(3):
        for j in range(2):
            A[i,j] = A[i+3,j+3] = src[i,j]
        A[i,j+1] = A[i+3,j+4] = 1
        
        b[i] = dst[i,0]
        b[i+3] = dst[i,1]
    
    cv.solve(A,b,X)

    h = 0
    for i in range(2):
        for j in range(3):
            M[i,j] = X[h]
            h +=1

    return M


