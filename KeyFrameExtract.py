import cv2
import numpy as np
#from matplotlib import pyplot as pt
#import statistics
i=0
S=0
m3=0
p=0
q=0
a=[0]*1000
b=[0]*1000

image=cv2.imread("/home/aman/Desktop/Mini-Project/Frames/frame0.jpg",cv2.IMREAD_COLOR)
cv2.imwrite("/home/aman/Desktop/Mini-Project/Frames/frame0.jpg", image)
while i<999:
    im1=cv2.imread("/home/aman/Desktop/Mini-Project/Frames/frame%d.jpg"%i,cv2.IMREAD_COLOR)
    im1=cv2.cvtColor(im1,cv2.COLOR_RGB2GRAY)

    im2=cv2.imread("/home/aman/Desktop/Mini-Project/Frames/frame%d.jpg"%(i+1),cv2.IMREAD_COLOR)
    im2=cv2.cvtColor(im2,cv2.COLOR_RGB2GRAY)
    m1=np.array(im1).astype(np.float32)
    m2=np.array(im2).astype(np.float32)
    m3=abs(m1-m2)

    S=np.sum(m3)
    a[i]=S
    i=i+1;

p=np.mean(a)
q=np.std(a)

th=p+2*q
i=0
j=0
while i<1000:
    l=int(a[i])
    #print(l,th,p,q)
    if l>th:
        img=cv2.imread("/home/aman/Desktop/Mini-Project/Frames/frame{0}.jpg".format(i+1),cv2.IMREAD_COLOR)
        cv2.imwrite("/home/aman/Desktop/Mini-Project/KeyFrames/frame{0}.jpg".format(j),img)
        j=j+1;
    i=i+1

	
	
	


