import cv2
import os
import shutil
from glob import glob

folderCounter = 1
folderBase = "FrameFolder"

def FrameCapture(path):
    global folderCounter
    vidObj = cv2.VideoCapture(path)
    success = 1
    count = 0
    folderName = folderBase + str(folderCounter)
    os.mkdir(folderName)
    folderCounter += 1
    while success:
        success, image = vidObj.read()
        pathname = folderName + "/frame" + str(count) + '.jpg'
        cv2.imwrite(pathname, image)
        count += 1


if __name__ == '__main__':
    for var in glob("/home/aman/Desktop/Mini-Project/VideoClips/*.mp4"):
        #print(var)
        FrameCapture(var)
#shutil.rmtree("VideoClips")