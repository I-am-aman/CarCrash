import cv2
import numpy as np
# import pylab as pl
# import glob
# import pandas as pd


# define gabor filter bank with different orientations and at different scales
def build_filters():
    filters = []
    ksize = 9
    # define the range for theta and nu
    for theta in np.arange(0, np.pi, np.pi / 8):
        for nu in np.arange(0, 6 * np.pi / 4, np.pi / 4):
            kern = cv2.getGaborKernel((ksize, ksize), 1.0, theta, nu, 0.5, 0, ktype=cv2.CV_32F)
            kern /= 1.5 * kern.sum()
            filters.append(kern)
    return filters


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

    # reading the input image
    imgg = cv2.imread("frame56.jpg",0)

    # initializing the feature vector
    feat = []

    # calculating the local energy for each convolved image
    for j in range(40):
        res = process(imgg, f[j])
        temp = 0
        for p in range(128):
            for q in range(128):
                #temp = int(temp) + int(res[p][q]) * int(res[p][q])
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
    print(len(feat))
# feat matrix is the feature vector for the image


#[0, 3867853, 5244740, 10316386, 4259480, 3778586, 0, 962285529, 968649700, 16973096, 5919950, 4738647, 0, 6327708, 789581624, 54826750, 15112905, 9807166, 0, 294539939, 985504043, 407562590, 106988332, 44414147, 0, 236328882, 714234998, 922342973, 447887705, 167245263, 0, 294540190, 985508025, 407562590, 106988332, 44414147, 0, 6327708, 789572110, 54826408, 0, 188025, 199072, 242022, 190398, 187796, 0, 3806363, 3839400, 378534, 235706, 213961, 0, 253138, 3298598, 710020, 384123, 311940, 0, 1717999, 3892443, 2153736, 1027644, 668517, 0, 1582748, 3120356, 3684159, 2325641, 1319495, 0, 1718000, 3892453, 2153736, 1027644, 668517, 0, 253138, 3298568, 710018]
