import cv2
import os
import shutil
from glob import glob

folderCounter = 1
folderBase = "FrameFolder"
num = 0


# Function to extract frames from videos
def FrameCapture(path):
    global folderCounter, num
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
    num += count


if __name__ == '__main__':
    for var in glob("/home/aman/Desktop/Mini-Project/VideoClips/*.mp4"):
        print(var)
        FrameCapture(var)
    print(num)
    shutil.rmtree("VideoClips")
