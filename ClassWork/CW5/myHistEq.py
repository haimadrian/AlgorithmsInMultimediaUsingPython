__author__ = "Haim Adrian"

import matplotlib
from myHistEqLogic import *

# Do it to see a new window when calling plt.show, and not within PyCharm.
matplotlib.use('TkAgg')


def histogramEqualization(img):
    img = np.float64(img)
    pdf = myPDF(img)
    if pdf is None:
        return None

    cdf = myCDF(pdf)
    return applyCDFFilter(img, cdf)


def histogramEqualization2(img):
    img = np.float64(img)
    pdf, binEdges = numpyPDF(img)
    if pdf is None:
        return None

    cdf = myCDF(pdf)
    return applyCDFFilter(img, cdf)


darkImg = cv2.imread("Dark Image.jpg")
giraffeImg = cv2.imread("Giraffe.jpg")
cImg = cv2.imread("ImgC.jpg")

img1 = histogramEqualization(darkImg)
img2 = histogramEqualization(giraffeImg)
img3 = histogramEqualization(cImg)

img4 = histogramEqualization2(darkImg)
img5 = histogramEqualization2(giraffeImg)
img6 = histogramEqualization2(cImg)

plt.figure('Assignment 1 - Histogram Equalization')
plot('Dark Image', darkImg, 331)
plot('Giraffe', giraffeImg, 332)
plot('ImgC', cImg, 333)
plot('My', img1, 334)
plot('My', img2, 335)
plot('My', img3, 336)
plot('numpy', img4, 337)
plot('numpy', img5, 338)
plot('numpy', img6, 339)
plt.show()
