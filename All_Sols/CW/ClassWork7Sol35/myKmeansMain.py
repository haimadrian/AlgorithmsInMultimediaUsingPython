__author__ = 'Dmitry Patashov'

import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import myKmeansLogic as km
import cv2

dataNum = 1  # 1-4
k = 3

currDir = os.getcwd()
knnDataAdd = currDir + '\\K means Data\\'
dataName = 'Data' + str(dataNum) + '.xlsx'
xl = pd.ExcelFile(knnDataAdd+dataName)
df = xl.parse("Sheet1")

data = np.asarray(df)

plt.figure()

plt.scatter(data[:,0], data[:,1], color='black')

plt.show()

labeledData = km.myKMeans(k, data)

plt.figure()

plt.scatter(labeledData[labeledData[:,0]==0,1], labeledData[labeledData[:,0]==0,2], color='blue')

plt.scatter(labeledData[labeledData[:,0]==1,1], labeledData[labeledData[:,0]==1,2], color='green')

plt.scatter(labeledData[labeledData[:,0]==2,1], labeledData[labeledData[:,0]==2,2], color='red')

plt.show()


img = cv2.imread(currDir + '\\Images\\1.jpg')

blurImg = cv2.GaussianBlur(np.float64(img), (5, 5), 0)

b,g,r = cv2.split(blurImg)

m,n = b.shape

x1 = np.reshape(b, (-1,1))
x2 = np.reshape(g, (-1,1))
x3 = np.reshape(r, (-1,1))

X = np.concatenate((x1,x2,x3), axis=1)

labeledX = km.myKMeans(2, X)

labelsIm = np.reshape(labeledX[:,0], (m,n))

labelsIm -= np.min(labelsIm)
labelsIm /= np.max(labelsIm)
labelsIm = np.uint8(labelsIm * 255)

plt.figure()

plt.subplot(121)
plt.axis('off')
plt.title('Image')
plt.imshow(img)

plt.subplot(122)
plt.axis('off')
plt.title('Segments')
plt.imshow(labelsIm, cmap='gray')

plt.show()
