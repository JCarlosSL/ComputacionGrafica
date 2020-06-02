import numpy as np
import cv2 as cv

def Threashold(img,l,r):
        rows,cols =img.shape
        newMatrix=[[] for i in range(rows)]
        for i in range(rows):
                for j in range(cols):
                        newMatrix[i].append(Change(img[i,j],l,r)) 
        return np.array(newMatrix)
def Change(val,l,r):
        if(l <= val <= r):
                return 255
        else:
                return 0

img = cv.imread('question_2.png',0)
new = Threashold(img,59,255)

cv.imwrite('newquestion1.png',new)
