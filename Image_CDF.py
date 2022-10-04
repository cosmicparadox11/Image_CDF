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
def plot_graph(x,y,title,xlab,ylab,type=None):
    if type==None:
        plt.plot(x,y)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title(title)
        plt.show()
    elif type=="bar":
        plt.bar(x,y)
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.title(title)
        plt.show()




if __name__ == "__main__":

    image = cv.imread("animated.png",0)
    intensity_val,frequency=image_histogram(image)
    freq=np.array(frequency)
    pdf=freq/freq.sum()
    cdf=pdf.cumsum()
    #########################################################
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
    ###########################################################
    plot_graph(intensity_val,frequency,'Histogram','intensity value','number of pixels',type="bar")
    plot_graph(intensity_val,pdf,'PDF','intensity value','PDF')
    plot_graph(intensity_val,cdf,'CDF','intensity value','CDF')


####################
