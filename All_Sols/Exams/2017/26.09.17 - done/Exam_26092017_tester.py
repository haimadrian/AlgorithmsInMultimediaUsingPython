from Exam_26092017 import *
import cv2

# Ex. 1
myDim = (3, 5)
myMat = myTensTnsor(myDim)
print myMat
print myTensTnsor(3)

# Ex. 2
myFolder = 'C:\Users'
noFolder = 'Hello World'
list1 = myFilesList(myFolder)
list2 = myFilesList()
list3 = myFilesList(noFolder)
list4 = myFilesList(4)
print list1, list2, list3, list4

# Ex. 3
img = cv2.imread('a.png')
myMed = myImageMedian(img)
print myMed

# Ex. 4
img = cv2.imread('a.png')
newImg = myImageNegative(img)
# cv2.imshow('Image2', newImg)
# cv2.imshow('Image', img)
# cv2.waitKey()

# Ex. 5
img = cv2.imread('img2.jpg')
# cv2.imshow('org', img)
# cv2.imshow('img', myFastToneReplacement(img, 0, 50, 255))

# Ex. 6
# myRGBsplit(img)

# Ex. 7
img = cv2.imread('d.JPG', 0)
# cv2.imwrite('e1.jpg', img)
# cv2.imwrite('e2.jpg', myMedianFilt(img, 1))

# Ex. 8
img = cv2.imread('e2.jpg', 0)
SharpenMask = np.array([[-1, -2, -1],
                        [-2, 13, -2],
                        [-1, -2, -1]])
# cv2.imwrite('f.jpg', myMaskKernel(img, SharpenMask))

# Ex. 9
img = cv2.imread('img2.jpg', 0)
myPlotShape(img)