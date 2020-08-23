__author__ = "Haim Adrian"

import matplotlib
from myCannyLogic import *

# Do it to see a new window when calling plt.show, and not within PyCharm.
matplotlib.use('TkAgg')


# 1. Apply Gaussian filter to smooth the image in order to remove the noise
# 2. Find the intensity gradients of the image
# 3. Apply non-maximum suppression to get rid of spurious response to edge detection
# 4. Apply double threshold to determine potential edges
# 5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other
#    edges that are weak and not connected to strong edges.
def cannyEdgeDetector(img):
    blur = myGaussianBlur(img)
    gradientX, gradientY = myGradient(blur)
    intensityGradient, phase = myPhase(gradientX, gradientY)
    nonMaxSuppress = myNonMaximumSuppression(intensityGradient, phase)
    doubleThresh, strong, weak = myDoubleThreshold(nonMaxSuppress, 0.1, 0.5)  # Play with the min/max to see more/less edges
    result = myHysteresis(doubleThresh, strong, weak)

    return result


# sys.setrecursionlimit(2500)  # Changes the depth of recursion limit
darkImg = np.float64(cv2.imread("Dark Image.jpg"))
darkImg += 50
darkImg /= np.max(darkImg) * 255
# giraffeImg = cv2.imread("Giraffe.jpg")
# cImg = cv2.imread("ImgC.jpg")

img1 = cannyEdgeDetector(darkImg)
# img2 = cannyEdgeDetector(giraffeImg)

# gray1 = cv2.cvtColor(darkImg, cv2.COLOR_BGR2GRAY)
# gauss1 = cv2.GaussianBlur(darkImg, (3, 3), 0)
gauss1 = myGaussianBlur(darkImg)
laplacian1 = cv2.Laplacian(gauss1, cv2.CV_64F)
sobel1 = cv2.Sobel(gauss1, cv2.CV_64F, 1, 1, ksize=5)

plt.figure('Assignment 2 - Canny Edge Detection')
plot('Original', normalizeImage(darkImg), 221)
plot('My', img1, 222)
plot('Laplacian', normalizeImage(laplacian1), 223)
plot('Sobel', normalizeImage(laplacian1), 224)
plt.subplots_adjust(0, 0, 1, 0.96, 0.05, 0.07)
plt.show()

plt.figure('Assignment 2 - Canny Edge Detection')
plot('My', img1, 111)
plt.show()
