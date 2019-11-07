import subprocess
import os
from glob import glob


def make_shots(var):
    os.mkdir("VideoClips")
    subprocess.run(["scenedetect", "-i", var, "-o", "/home/aman/Desktop/Mini-Project/VideoClips", "detect-content",
                    "-t", "27", "split-video"])


if __name__ == '__main__':

    for var in glob("/home/aman/Desktop/Mini-Project/RoadAccidents/testVideo*.mp4"):

        make_shots(var)
        os.system("python FrameExtract.py")
        os.system("python KeyFrameExtract.py")
        os.system("python GaborFeatureExtraction.py")

