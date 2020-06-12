import numpy as np

class subtraccion:
    def __init__(self,_img):
        self.img=_img


    def subtraccionImg(self,imgs):
        self.img=self.img.astype(int)
        imgs=imgs.astype(int)
        rows,cols = self.img.shape

        newmatrix=[ [] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                newmatrix[i].append((self.img[i,j]-imgs[i,j])%256)

        return np.array(newmatrix)

    def subtraccionC(self,c=0):
    	self.img=self.img.astype(int)
    	rows,columns = self.img.shape;
    	
    	newmatrix = [ [] for i in range(rows)]
    	for i in range(rows):
    		for j in range(columns):
    			newmatrix[i].append((self.img[i,j]-c)%256)
    	return np.array(newmatrix)
