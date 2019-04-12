import cv2
import numpy as np
import os
import glob
import shutil

os.mkdir("KeyFrames")
counter = 0

for name in glob.glob("/home/aman/Desktop/Mini-Project/FrameFolder*"):
    print(name)
    num=len([f for f in os.listdir(name)])
    a=[0]*num
    b=[0]*num
    count=0
    mean=0
    deviation=0
    i=0;
    while i<num-2:
        FirstImage=name+"/frame"+str(i)+'.jpg'
        im1 = cv2.imread(FirstImage, cv2.IMREAD_COLOR)
        im1 = cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY)

        SecondImage=name+"/frame"+str(i+1)+'.jpg'
        im2 = cv2.imread(SecondImage, cv2.IMREAD_COLOR)
        im2 = cv2.cvtColor(im2, cv2.COLOR_RGB2GRAY)

        FirstArray = np.array(im1).astype(np.float32)
        SecondArray = np.array(im2).astype(np.float32)
        Difference = abs(FirstArray - SecondArray)

        Sum = np.sum(Difference)
        a[i] = Sum
        i = i + 1;

    mean = np.mean(a)
    deviation = np.std(a)
    th = mean + 1.2 * deviation

    i = 0
    while i < num-1:
        l = int(a[i])
        if float(l) > th:
            path=name+"/frame"+str(i+1)+'.jpg'
            img = cv2.imread(path,cv2.IMREAD_COLOR)
            cv2.imwrite("/home/aman/Desktop/Mini-Project/KeyFrames/frame{0}.jpg".format(counter), img)
            counter += 1;
            #print(j)
        i = i + 1
    #shutil.rmtree(name)