import numpy as np
import cv2 as cv

def Pdistribucion(hist,totalPixel):
	vP=[]
	for i in range(len(hist)):
		vP.append(hist[i]/totalPixel)
	return vP


def sumDistribucion(vP):
	sumD=[]
	temp=0
	for i in range(len(vP)):
		sumD.append(vP[i]+temp)
		temp+=vP[i]
	return sumD

def functionS(Fxy,sumD,L):
        return (L-1)*sumD[Fxy]

def HistogramEqualizer(img):
	hist,bins = np.histogram(img.flatten(),256,[0,256])
	rows,columns = img.shape
	vP = Pdistribucion(hist,rows*columns)
	sumD = sumDistribucion(vP)

	newimg=[[] for i in range(rows)]
	for i in range(rows):
		for j in range(columns):
			newimg[i].append(functionS(img[i,j],sumD,256))
	return np.array(newimg)

   
img = cv.imread('question_1.png',0)
new = HistogramEqualizer(img)

cv.imwrite('newquestion1.png',new)
