import cv2
import numpy as np
import os
import glob
import shutil

os.mkdir("KeyFrames")
counter = 0

for name in glob.glob("/home/aman/Desktop/Mini-Project/FrameFolder*"):
    print(name)
    numOfFrames = len([f for f in os.listdir(name)])
    sumOfDiffArray = [0]*numOfFrames
    count = 0
    mean = 0
    deviation = 0
    i = 0;
    while i<numOfFrames-2:
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
        sumOfDiffArray[i] = Sum
        i = i + 1

    mean = np.mean(sumOfDiffArray)
    deviation = np.std(sumOfDiffArray)
    if numOfFrames < 20:
        constant = 0.1
    else:
        constant = 1.5

    th = constant*mean + deviation
    i = 0
    while i < numOfFrames-1:
        l = int(sumOfDiffArray[i])
        if float(l) > th:
            path = name+"/frame"+str(i+1)+'.jpg'
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            cv2.imwrite("/home/aman/Desktop/Mini-Project/KeyFrames/frame{0}.jpg".format(counter), img)
            counter += 1
        i = i + 1

    shutil.rmtree(name)
print(counter)