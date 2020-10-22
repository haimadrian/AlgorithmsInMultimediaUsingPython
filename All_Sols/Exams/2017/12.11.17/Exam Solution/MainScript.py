__author__ = 'Dmitry Patashov'

import FunctionsScript as fs
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('ImgC.jpg')
imgG = cv2.imread('ImgC.jpg', 0)

# Question 1

# myDim = (3,5)
# print 'Question 1 - Test 1'
# print fs.myFullTensor(myDim)
# myList = [3,5]
# print 'Question 1 - Test 2'
# print fs.myFullTensor(myList)
# print '\n'
#
# # Question 2
#
# print 'Question 2 - Test 1'
# print fs.myFilesList()
# print 'Question 2 - Test 2'
# print fs.myFilesList('Hello World')
# print 'Question 2 - Test 3'
# print fs.myFilesList('C:\\')
# print '\n'

# Question 3

# myTuple = (3,5)
# print 'Question 3 - Test 1'
# print fs.myImageMean(myTuple)
# print 'Question 3 - Test 2'
# print fs.myImageMean(img)
# print 'Question 3 - Test 3'
# print fs.myImageMean(np.array([[1,3],[3,5]]))
# print '\n'

# Question 4

myMat = np.array([[1,1,1],
                  [2,7,3],
                  [7,7,7]])
print 'Question 4 - Test 1'
# print fs.myCommonTone(myMat)
print 'Question 4 - Test 2'
# print fs.myCommonTone(myTuple)
print 'Question 4 - Test 3'
print fs.myCommonTone(imgG)
print '\n'

# # Question 5
#
# print 'Question 5 - Test 1'
# plt.figure()
# plt.subplot(121)
# plt.imshow(img[:,:,::-1])
# plt.subplot(122)
# plt.imshow(fs.myLine(img)[:,:,::-1])
# plt.show()
# print '\n'
#
# # Question 6a
#
# myMat = np.round(np.random.uniform(0, 180, (5,5)) * 100) / 100
# print 'Question 6 - Test 1'
# print myMat, '\n'
# print fs.myPhaseRound(myMat)
# print '\n'
#
# # Question 7
#
# myData = np.concatenate((np.concatenate((np.ones((5,10)) * 5, np.ones((2,10)) * 2), axis=0), np.ones((3,10)) * 3), axis=0)
# FullData = myData.copy()
# for i in range(9):
#     FullData = np.concatenate((FullData,myData))
#
# print 'Question 7 - Test 1'
# TrData, TeData, ValData = fs.myDataSplit(FullData)
# print 'TrData: ', np.float64(np.max(TrData) + np.min(TrData))/2
# print 'TeData: ', np.float64(np.max(TeData) + np.min(TeData))/2
# print 'ValData: ', np.float64(np.max(ValData) + np.min(ValData))/2
# print '\n'
#
# # Question 8
#
# funName = 'All'
# print 'Question 8 - Test 1'
# print fs.myFunctionPlotter(funName)
# print 'Question 8 - Test 2'
# print fs.myFunctionPlotter('Hello Python')
# print '\n'
#
# # Question 9
#
# print 'Question 9 - Test 1'
# fs.myPlotShape(imgG)
