__author__ = 'Dmitry Patashov'

import FunctionsScript as fs
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('ImgC.jpg')
imgG = cv2.imread('ImgC.jpg', 0)
imgN = cv2.imread('img.png', 0)
imgD = cv2.imread('imgD.jpg')

# Question 1
# print 'Question 1 - Test 1'
# print fs.myIdentityMatrix(5)
# print '\n'

# Question 2
# print 'Question 2 - Test 1'
# myList = [1, [3.1], 6.0, 'number', (13, 3), ['hello', 8], np.uint8(12), '20']
# print fs.myArrayMean(myList)
# print '\n'

# # Question 3
# print 'Question 3 - Test 1'
# k = 3
# x = -1.2
# myArray = np.array([-3.2, 8, 1, 0, -1.1, 0.1, 12])
# print fs.myKNearest(k, x, myArray)
# print '\n'

# # Question 4
# print 'Question 4 - Test 1'
# print fs.myDirLongName()
# print '\n'
#
# # Question 5
# print 'Question 5 - Test 1'
# plt.figure()
# plt.subplot(121)
# plt.imshow(img[:,:,::-1])
# plt.axis('off')
# plt.subplot(122)
# plt.imshow(fs.myFastToneReplacement(img, 57, 173, 77)[:,:,::-1])
# plt.axis('off')
# plt.show()
# print '\n'

# # Question 6
# print 'Question 6 - Test 1'
# plt.figure()
# plt.subplot(121)
# plt.imshow(imgN, cmap='gray')
# plt.axis('off')
# plt.subplot(122)
# plt.imshow(fs.myMedianFilt(imgN, 2), cmap='gray')
# plt.axis('off')
# plt.show()
# print '\n'
#
# # Question 7
# myMat = np.round(np.random.uniform(0, 180, (5,5)) * 100) / 100
# print 'Question 7 - Test 1'
# print myMat, '\n'
# print fs.myPhaseRound(myMat)
# print '\n'
#
# # Question 8
print fs.myHistEq(imgD)
# print 'Question 8 - Test 1'
# plt.figure()
# plt.subplot(121)
# plt.title('Original Image')
# plt.axis('off')
# plt.imshow(imgD, vmin = 0, vmax = 255)
# plt.subplot(122)
# plt.title('Histogram Equalization')
# plt.axis('off')
# plt.imshow(fs.myHistEq(imgD), vmin = 0, vmax = 255)
# plt.show()
# print '\n'
#
# # Question 9
# print 'Question 9 - Test 1'
# fs.myPlotShape(imgG)

