import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv

def image_histogram(image):
    m,n =image.shape
    intensity_val=[]
    frequency=[]
    for val in range(256):
        freq=0
        intensity_val.append(val)
        freq=(image==val).sum()
        frequency.append(freq)
    return intensity_val,frequency


image = cv.imread("animated.png",0)
intensity_val,frequency=image_histogram(image)
freq=np.array(frequency)
pdf=freq/freq.sum()
cdf=pdf.cumsum()
#############################################################################
"""PDF and CDF without numpy"""
sum_freq=0
pdf1=[]
for freq in frequency:
    sum_freq+=freq
for freq in frequency:
    pdf1.append(freq/sum_freq)
cumsum=0
cdf1=[]
for i in pdf1:
    cumsum+=i
    cdf1.append(cumsum)
#############################################################################
figure, axis = plt.subplots(3,1)
axis[0].bar(intensity_val,frequency)
axis[0].set_xlabel('intensity value')
axis[0].set_ylabel('number of pixels')
axis[0].set_title('Histogram')

axis[1].plot(intensity_val,pdf)
axis[1].set_xlabel('intensity value')
axis[1].set_title('PDF')

axis[2].plot(intensity_val,cdf)
axis[2].set_xlabel('intensity value')
axis[2].set_title('CDF')

plt.tight_layout()
plt.show()