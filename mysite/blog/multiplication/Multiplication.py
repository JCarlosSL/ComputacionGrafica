import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

class MultiplicationOperator:
    def __init__(self,_img):
        self.img=_img
        self.rows=_img.shape[0]
        self.cols=_img.shape[1]
        self.newimg = [ [] for i in range(self.rows)]
    def mult(self,p,q):
        return np.multiply(p,q)

    def multiplicacionImg(self,imgs):
        self.img = self.img.astype(int)
        for i in range(self.rows):
            for j in range(self.cols):
                self.newimg[i].append(self.mult(self.img[i,j],imgs[i,j]))

        imgn = np.array(self.newimg)
        imgn[np.where(imgn > 255)] = 255
        return imgn.astype(np.uint8)

    def MultiplicacionC(self,c=1):
        self.img =self.img.astype(int)
        for i in range(self.rows):
            for j in range(self.cols):
                self.newimg[i].append(self.mult(self.img[i,j],c))
        
        imgn = np.array(self.newimg)
        imgn[np.where(imgn > 255)] = 255
        return imgn.astype(np.uint8)
"""
img = cv.imread('mul_4.jpg')
MO = MultiplicationOperator(img)

imgout = MO.MultiplicacionC(3)
print(imgout)
cv.imwrite('imgout.png',imgout)
"""


