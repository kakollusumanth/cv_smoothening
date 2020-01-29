import cv2
import numpy as np
from matplotlib import pyplot as plt
#img=cv2.imread(r'temp.jpg')       
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.boxFilter(img,-1,(5,5))
g_blur=cv2.GaussianBlur(img,(5,5),0)
m_blur=cv2.medianBlur(img,5)
bilateralfilter=cv2.bilateralFilter(img,9,75,75)
titles=['img','2d_convolution','blur','gblur','mblur','bilateral']
images=[img,dst,blur,g_blur,m_blur,bilateralfilter]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()               
                   
