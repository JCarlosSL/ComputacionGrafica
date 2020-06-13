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
        return np.multiply(p,q).astype(np.uint8)

    def multiplicacionImg(self,imgs):
    	self.img=self.img.astype(int)
    	imgs=imgs.astype(int)
    	for i in range(self.rows):
    		for j in range(self.cols):
    			self.newimg[i].append(self.mult(self.img[i,j],imgs[i,j]))
    	return np.array(self.newimg)

    def MultiplicacionC(self,c=1):
    	self.img=self.img.astype(np.uint8)
    	for i in range(self.rows):
    		for j in range(self.cols):
    			self.newimg[i].append((self.img[i,j]*c))
    	return np.array(self.newimg).astype(np.uint8)



