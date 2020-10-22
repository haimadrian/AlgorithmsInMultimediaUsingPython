__author__ = 'Alon Ziv'

from Exam_27092016 import *
from matplotlib import pyplot as plt

# Ex. A1
# print remomve_symbol('abc', 3), remomve_symbol('abc', 1), remomve_symbol('abc', 2)

# Ex. A2
# l = range(1,26)
# print list2matrix(l, 12), list2matrix(l, 5)

# Ex. A3
# print create_3darray((2, 2, 2)), create_3darray((0, 1, 2)), create_3darray((1, 2)), create_3darray(('a', 2))

# Ex. A4
# print count_word('abc, abc,abc', 'abc')

# Ex. B1
# img = cv2.imread('img2.jpg', 0)
# cv2.imwrite('i.jpg', PadMyImage(img, 30))

# Ex. B2
# img = cv2.imread('d.JPG', 0)
# mask = np.array([[-1, 0, 1],
#                  [-1, 0, 1],
#                  [-1, 0, 1]])
# plt.figure()
# plt.imshow(MaskMyImage(img, mask), cmap='gray')
# plt.show()

# Ex. B3
# FunctionPlotter('All')

# Ex. B4
img = cv2.imread('img2.jpg', 0)
MyCirclePlot(img)