import numpy as np

class divisionOperator:
    def __init__(self,_img):
        self.img=_img
        self.rows = _img.shape[0]
        self.cols = _img.shape[1]
        self.newimg = [ [] for i in range(self.rows)]

    def div(self,p,q):
        return np.divide(p,q).astype(np.uint8)

    def divisionImg(self,imgs):

        for i in range(self.rows):
            for j in range(self.cols):
                self.newimg[i].append(self.div(
                    self.img[i,j],imgs[i,j]))

        #self.rescaling()
        return np.array(self.newimg)

    def divisionC(self,c=1):

        for i in range(self.rows):
            for j in range(self.cols):
                self.newimg[i].append(self.div(
                    self.img[i,j],c))

        #self.rescaling()
        return np.array(self.newimg)
        
    def funcrescaling(self,fxy):
        return ((fxy-self.nmin)*(255/(self.nmax-self.nmin)))

    def rescaling(self,nmin=0,nmax=255):

        self.nmin=np.min(self.img)
        self.nmax=np.max(self.img)
        self.newimgr = [ [] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.newimgr[i],append(self.funcrescaling(self.newimg[i,j]))
