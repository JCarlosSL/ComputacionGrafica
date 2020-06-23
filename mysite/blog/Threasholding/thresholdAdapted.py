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

"""
vecinos = [[1,-1],[-1,0],[-1,+1],[0,-1],[0,+1],[+1,-1],[+1,0],[+1,+1]]
"""
size_vecinos=len(vecinos)

class ThresholdAdaptativo:

    def __init__(self,_img):
        self.img=_img;
        self.rows = self.img.shape[0]
        self.cols = self.img.shape[1]
    

    def Threshold(self,c):
        new_Matrix= [[] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                new_Matrix[i].append(self.change(self.promedio(i,j)-c,self.img[i,j]))

        return np.array(new_Matrix)
    
    def promedio(self,h,k):
        suma=0
        s=0
        x=self.rows
        y=self.cols
        for i in range(size_vecinos):
            if(0<=h+vecinos[i][0] < x and 0<=k+vecinos[i][1]< y):
                suma+=self.img[h+vecinos[i][0],k+vecinos[i][1]]
                s+=1
        prom=(suma + self.img[h,k])/(s+1)
        return prom

    def change(self,prom, limite):
        if(prom<limite):
            return 255
        else:
            return 0
"""
img = cv.imread('paper6.jpg',0)
th = ThresholdAdaptativo(img)
new = th.Threshold(5)
cv.imwrite('newpapere.png',new)"""
