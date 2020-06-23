import numpy as np
import cv2 as cv

class affine:

    def __init__(self):
        self.B = np.matrix([[0],[0]])
        self.A = np.matrix([[1,0],[0,1]])

    def F(self,fxy):
        fxy1=self.A*fxy.T + self.B
        return int(fxy1[0,0]),int(fxy1[1,0])

    def setup(self,M):
        self.A = M[0:2,0:2]
        self.B = M[0:2,2:]

    def warpAffine(self,img,M,rows,cols):
        self.setup(M)

        newimg = np.zeros((rows,cols,3))
        for i in range(rows):
            for j in range(cols):
                i_1,j_1=self.F(np.matrix([i,j]))
                if(i_1 >= rows or j_1>= cols): break; 
                newimg[i_1,j_1] = img[i,j]

        return newimg

    def Mtranslate(self,p=[0,0]):
        return np.matrix([[1,0,p[0]],[0,1,p[1]]])

    def Mscale(self,p=[0,0]):
        return np.matrix([[1+p[0],0,0],[0,p[1],0]])

    def Mrotate(self,theta=45,p=[0,0]):
        cos = np.cos(theta)
        sen = np.sin(theta)
        return np.matrix([[cos,sen,(1-cos)*p[0]-sen*p[1]],
                [-sen,cos,sen*p[0]+(1-sen)*p[1]]])

    def Mshear(self,p=[0,0]):
        return np.matrix([[1,p[0],0],[p[1],1,0]])


