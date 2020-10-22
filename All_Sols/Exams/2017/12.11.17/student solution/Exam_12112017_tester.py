__author__ = 'Alon Ziv'

from Exam_12112017 import *
import numpy, cv2

# Ex. 1
# print myFullTensor((3, 5)), myFullTensor('a'), myFullTensor(('a', 3)), myFullTensor((-3))

# Ex. 2
# print myFilesList('C:\Users'), myFilesList(), myFilesList('Hello World'), myFilesList(4)

# Ex. 3
# img = cv2.imread('img2.jpg')
# print myImageMean(img)

# Ex. 4
# img = cv2.imread('img2.jpg', 0)
# print myCommonTone(img)

# Ex. 5
# img = cv2.imread('d.jpg')
# cv2.imwrite('img222.jpg', myLine(img))

# Ex. 6
# mat = np.random.uniform(0, 180, (5, 5))
# mat[1, 0], mat[0, 0], mat[0, 1], mat[1, 1] = 180, 22, 23, 112.99429894
# print mat, '\n', myPhaseRound(mat)

# Ex. 7
# mat = np.random.uniform(1, 100, (100, 1))
# a, b, c = myDataSplit(mat)
# print 'mat:\n', mat, '\na:\n', a, '\nb:\n', b, '\nc:\n', c

# Ex. 8
# myFunctionPlotter('All')

# Ex. 9
img = cv2.imread('img2.jpg', 0)
myPlotShape(img)
