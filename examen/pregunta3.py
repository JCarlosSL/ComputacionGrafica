import numpy as np
import cv2 as cv

vecinos=[[-1,-1],[-1,0],[-1,+1],
        [0,-1],[0,+1],
        [+1,-1],[+1,0],[+1,+1],
        [-2,-2],[-2,-1],[-2,0],[-2,+1],[-2,+2],
        [-1,-2],[-1,+2],
        [0,-2],[0,+2],
        [+1,-2],[+1,+2],
        [+2,-2],[+2,-1],[+2,0],[+2,+1],[+2,+2]]

def promedio(img,h,k):
    n=len(vecinos)
    suma=0
    x,y = img.shape
    s=0
    for i in range(n):
        if(0 <= h+vecinos[i][0] < x and 0<= k+vecinos[i][1] < y ):
            suma+=img[h+vecinos[i][0],k+vecinos[i][1]]
            s+=1;
    prom=suma/s
    return prom+255

def Threashold(img,C=0,l=0,r=0):
        rows,cols =img.shape
        newMatrix=[[] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                newMatrix[i].append(change((promedio(img,i,j)-C)%256,l,r)) 
        return np.array(newMatrix)

def change(pixel,l=0,r=0):
    if l<pixel<r:
        return 0
    else:
        return 255

img = cv.imread('question_3.png',0)
new = Threashold(img,50,100,180)

cv.imwrite('newquestion3.png',new)
