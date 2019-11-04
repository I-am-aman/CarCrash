import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from collections import Counter, defaultdict


# define gabor filter bank with different orientations and at different scales
def build_filters():
    gaborfilters = []
    ksize = 9
    # define the range for theta and nu
    for theta in np.arange(0, np.pi, np.pi / 8):
        for nu in np.arange(0, 6 * np.pi / 4, np.pi / 4):
            kern = cv2.getGaborKernel((ksize, ksize), 1.0, theta, nu, 0.5, 0, ktype=cv2.CV_32F)
            kern /= 1.5 * kern.sum()
            gaborfilters.append(kern)
    # print(gaborfilters)
    # print(len(gaborfilters))
    return gaborfilters


# function to convolve the image with the filters
def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum


if __name__ == '__main__':

    # instantiating the filters
    filters = build_filters()

    f = np.asarray(filters)

    allKeyFramesFeat = []

    numOfKeyFrames = len([f for f in os.listdir("/home/aman/Desktop/Mini-Project/KeyFrames/")
                          if os.path.isfile(os.path.join("/home/aman/Desktop/Mini-Project/KeyFrames/", f))])
    # print(numOfKeyFrames)
    counter = 0
    while counter < numOfKeyFrames:
        print("Processing for KeyFrame{0}".format(counter))
        # reading the input image
        imgg = cv2.imread("/home/aman/Desktop/Mini-Project/KeyFrames/frame{0}.jpg".format(counter), 0)

        # initializing the feature vector
        feat = []

        # calculating the local energy for each convolved image
        for j in range(40):
            res = process(imgg, f[j])
            temp = 0
            for p in range(128):
                for q in range(128):
                    temp = temp + res[p][q] * res[p][q]
            feat.append(temp)

        # calculating the mean amplitude for each convolved image
        for j in range(40):
            res = process(imgg, f[j])
            temp = 0
            for p in range(128):
                for q in range(128):
                    temp = temp + abs(res[p][q])
            feat.append(temp)
        print(feat)
        # print(len(feat))
        allKeyFramesFeat.append(feat)
        counter += 1

    print(allKeyFramesFeat)
    print(len(allKeyFramesFeat))

    kmeans = KMeans(n_clusters=5, random_state=0).fit(allKeyFramesFeat)
    print(kmeans.labels_)
    #print(kmeans.cluster_centers_)

    vectorForVideo = []
    for eachCentroid in kmeans.cluster_centers_:
        vectorForVideo.extend(eachCentroid)

    counter = Counter(kmeans.labels_)
    sorted(counter.items())
    print(counter)
    for i in range(5):
        vectorForVideo.append(counter[i])

    print(vectorForVideo)
    print(len(vectorForVideo))

    # plt.scatter(allKeyFramesFeat[:, 0], allKeyFramesFeat[:, 1], c=kmeans.labels_, cmap='rainbow')
    # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
# feat matrix is the feature vector for the image
