import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def Threshold(img, l,r):
	rows,cols = img.shape
	matrixOut = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			matrixOut[i].append(FuncThreshold(l,r,img[i,j]))
	return matrixOut

def FuncThreshold(l,r,pixVal):
	if(l < pixVal and pixVal < r):
		return 0
	else:
		return 255

def ContrastS(img,a,b,c,d):
	rows,cols = img.shape
	matrixOut = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			px = 0
			if(c < img[i,j] and img[i,j] < d):
				px = img[i,j]
			else:
				px = ((d-c)/2)+c
			matrixOut[i].append((FuncContrastS(a,b,c,d,px)))
	return matrixOut

def FuncContrastS(a,b,c,d,px):
	return (((px-c)*((b-a)/(d-c)))+a)

def Subt(imgA,imgB):
	imgA = imgA.astype(int)
	imgB = imgB.astype(int)
	rows,cols = imgA.shape
	matrixOut = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			matrixOut[i].append(((imgA[i,j] - imgB[i,j])%255))
	return matrixOut

def Add(imgA,imgB):
	imgA = imgA.astype(int)
	imgB = imgB.astype(int)
	rows,cols = imgA.shape
	matrixOut = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			matrixOut[i].append(((imgA[i,j] + imgB[i,j])%255))
	return matrixOut


##### ejercicio 3 perra 

addressA = 'sub_1.jpg'
addressB = 'sub_2.jpg'
imgA = cv.imread(addressA,0) 
imgB = cv.imread(addressB,0) 

OutPut = Subt(imgA,imgB) ###hasta aqui es resta abajo es cascada con thresold
endput = np.array(OutPut)
OutPut2 = Threshold(endput,70,235)

plt.imshow(OutPut2,'gray')
plt.show()


##### ejercicio 4 recontra perraaa
"""
addressA = 'sub_10.jpg'
addressB = 'sub_11.jpg'
imgA = cv.imread(addressA,0) 
imgB = cv.imread(addressB,0) 

OutPut = Sub(imgA,imgB) ### hasta aqui es resta abajo es cascada con contrast
OutPut2 = ContrastS(np.array(OutPut),0,255,30,235)
plt.imshow(OutPut2,'gray')
plt.show()
"""
