import numpy as np
import cv2 as cv

class affine:

    def __init__(self):
        self.B = np.matrix([[0],[0]])
        self.A = np.matrix([[1,0],[0,1]])

    def F(self,fxy):
        fxy1=self.A*fxy.T + self.B
        return int(fxy1[0,0]),int(fxy1[1,0])

    def Finverso(self,fuv):
        y = fuv-self.B
        fuv1 = self.A*(y)
        return int(fuv1[0,0]),int(fuv1[1,0])

    def setupM(self,M):
        self.A = M[0:2,0:2].I
        self.B = M[0:2,2:]

    def warpAffine(self,img,M,rows,cols):
        self.setupM(M)
        r,c = img.shape[0],img.shape[1]
        newimg = np.zeros((cols,rows,3)).astype(np.uint8)
 
        for u in range(cols):
            for v in range(rows):
                j,i=self.Finverso(np.matrix([[u],[v]]))
                if(0 < i < r and 0 < j < c):
                    newimg[u,v] = img[i,j]
        
        return newimg

    def Mtranslate(self,p=[0,0]):
        return np.matrix([[1,0,p[0]],[0,1,p[1]]])

    def Mscale(self,p=[0,0]):
        return np.matrix([[p[0],0,0],[0,p[1],0]])

    def Mrotate(self,theta,px,py):
        r = np.pi
        theta1 = (r/180)*theta
        cos = np.cos(theta1)
        sen = np.sin(theta1)
        return np.matrix([[cos,sen,(1-cos)*px-sen*py],
                [-sen,cos,sen*px+(1-cos)*py]])

    def Mshear(self,p=[0,0]):
        return np.matrix([[1,p[0],0],[p[1],1,0]])

    def rotacion(self,px,py,M,r,c):
                
        cos = np.abs(M[0,0])
        sen = np.abs(M[0,1])

        co = int(r*sen + c*cos)
        ro = int(r*cos + c*sen)

        M[0,2] += ((co/2) - px)
        M[1,2] += ((ro/2) - py)

        return ro,co


