__author__ = 'Alon Ziv'

from Exam_10012018 import *
import numpy, cv2

# Ex. 1
# print myIdentityMatrix(3), myIdentityMatrix(-3), myIdentityMatrix('a')

# Ex. 2
# print myArrayMean([1, [3.1], 2.0, 'number', (13, 3), ['hello', 8], np.uint8(12), '20'])

# Ex. 3
# print myKNearest(3, -1.2,  numpy.array([-3.2, 8, 1, 0, -1.1, 0.1, 12]))

# Ex. 4
# print myDirLongName()

# Ex. 5
# img = cv2.imread('bb.png')
# cv2.imwrite('bbnew.png', myFastToneReplacement(img, 99, 100, 200))

# Ex. 6
# img = cv2.imread('img2.jpg', 0)
# cv2.imwrite('img21.jpg', img)
# cv2.imwrite('img22.jpg', myMedianFilt(img, 1))

# Ex. 7
# myMat = np.uint8(np.random.uniform(0, 180, (5, 5)))
# myMat[0, 0] = 180
# myMat[0, 1] = 22
# myMat[0, 2] = 23
# print myMat, '\nnew mat\n', myPhaseRound(myMat)

# Ex. 8
# img = cv2.imread('img2.jpg')
# img = np.uint8(np.round(img))
# cv2.imwrite('img2a.jpg', myHistEq(img))

# Ex. 9
img = cv2.imread('img2.jpg', 0)
myPlotShape(img)