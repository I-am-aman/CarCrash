import subprocess
import os
from glob import glob
import csv

# Function to make shots
def make_shots(var):
    os.mkdir("VideoClips")
    subprocess.run(["scenedetect", "-i", var, "-o", "/home/aman/Desktop/Mini-Project/VideoClips", "detect-content",
                    "-t", "27", "split-video"])


if __name__ == '__main__':

    try:
        os.remove("feature_vector.csv")
        os.remove("label_vector.csv")
    except OSError:
        pass

    labelvector = []

    # Running algorithm for Accident Videos
    for var in glob("/home/aman/Desktop/Mini-Project/RoadAccidents/RoadAccident*.mp4"):

        print(var)
        make_shots(var)
        os.system("python FrameExtract.py")
        os.system("python KeyFrameExtract.py")
        os.system("python GaborFeatureExtraction.py")
        labelvector.append(1)

    # Running algorithm for Non-Accident Videos
    for var in glob("/home/aman/Desktop/Mini-Project/NonAccidents/videoplayback*.mp4"):

        print(var)
        make_shots(var)
        os.system("python FrameExtract.py")
        os.system("python KeyFrameExtract.py")
        os.system("python GaborFeatureExtraction.py")

        labelvector.append(0)

    # Making label_vector.csv
    with open("label_vector.csv", 'a') as outfile:
        writer = csv.writer(outfile, delimiter=' ')
        writer.writerow(labelvector)

    # Reading feature_vector.csv file for checking purpose
    # readlist = []
    # with open("feature_vector.csv", 'r') as my_file:
    #     reader = csv.reader(my_file, delimiter=' ')
    #     readlist = list(reader)
    #
    # new_list = [list(map(float, lst)) for lst in readlist]
    # print(new_list)
