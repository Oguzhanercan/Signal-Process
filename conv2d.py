import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open("C:/Users/bilgisayar/Desktop/Conv_TUTO/resimler/tacmahal.jpg")
img = np.asarray(img)
img = np.mean(img,axis = 2)
filter = np.matrix([[0,0,0,0,0],
                   [0,2,0,-2,0],
                   [0,2,0,-2,0],
                   [0,2,0,-2,0],
                   [0,0,0,0,0]]
                  )
def padding_zero2d(img,padsize):#padding
    return np.pad(img, (padsize,),  mode='constant', constant_values=0)
img_filtered = np.zeros_like(img)

def conv2d(img,padsize,stride,img_filtered):
    img_pad = padding_zero2d(img,padsize)
    for j in range(0,img.shape[0],stride):
        for i in range(0,img.shape[1],stride):
            img_filtered[j,i] = (np.multiply(filter,img_pad[j:j+filter.shape[0],i : i+filter.shape[1]])).sum()
    return img_filtered

img_filtered = conv2d(img,2,1,img_filtered)
plt.imshow(img_filtered,cmap = "gray")
plt.show()