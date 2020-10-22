__author__ = 'Dmitry Patashov'

import os
import cv2
from matplotlib import pyplot as plt
import myCannyLogic as cl
import numpy as np

CurDir = os.getcwd()
ImgAdd = CurDir + '\Images\\'

img = cv2.imread(ImgAdd+'ImgC.jpg')

lowThreshold = 0
highThreshold = 0

# Gaussian Blur
imgGB = cl.GaussBlur(img)

imgGB = imgGB - np.min(imgGB)
imgGB = imgGB / np.max(imgGB)
imgGB = np.round(imgGB * 255)

# Phase and Gradient
GradX, GradY = cl.SobelMasking(imgGB)

IGrad = (GradX ** 2 + GradY ** 2) ** 0.5

PhaseMat = cl.PhaseMatrixCalculation(GradX, GradY)

# Non-Maximum suppression
cPhaseMat = cl.NonMaximumSuppressionStep1(PhaseMat.copy())

nmsIGrad = cl.NonMaximumSuppressionStep2(IGrad, cPhaseMat)

# Double threshold

edgeMap = cl.DoubleThresholding(nmsIGrad, lowThreshold, highThreshold)

# Track Edges by Hysteresis

EdgeBinMap = cl.TrackEdgesByHysteresis(edgeMap)

# Canny Compare

CannyGradX = GradX * EdgeBinMap
CannyGradY = GradY * EdgeBinMap

CannyIGrad = (CannyGradX ** 2 + CannyGradY ** 2) ** 0.5

CannyIGrad = CannyIGrad - np.min(CannyIGrad, axis=(0,1))
CannyIGrad = CannyIGrad / np.max(CannyIGrad, axis=(0,1)) * 255
CannyIGrad = np.uint8(CannyIGrad)


SobelGradX, SobelGradY = cl.SobelMasking(img)
SobelIGrad = (SobelGradX**2 + SobelGradY**2)**0.5

SobelIGrad = SobelIGrad - np.min(SobelIGrad, axis=(0,1))
SobelIGrad = SobelIGrad / np.max(SobelIGrad, axis=(0,1)) * 255
SobelIGrad = np.uint8(SobelIGrad)


LaplacianMask = np.array([[0,-1,0],
                          [-1,4,-1],
                          [0,-1,0]], dtype=np.float64)

LaplacianIGrad = cv2.filter2D(np.float64(img.copy()),-1,LaplacianMask)

LaplacianIGrad = np.abs(LaplacianIGrad)
LaplacianIGrad = LaplacianIGrad - np.min(LaplacianIGrad, axis=(0,1))
LaplacianIGrad = LaplacianIGrad / np.max(LaplacianIGrad, axis=(0,1)) * 255
LaplacianIGrad = np.uint8(LaplacianIGrad)

plt.figure()

plt.subplot(211)
plt.axis('off')
plt.title('Canny')
plt.imshow(CannyIGrad[:,:,::-1])

plt.subplot(223)
plt.axis('off')
plt.title('Sobel')
plt.imshow(SobelIGrad[:,:,::-1])

plt.subplot(224)
plt.axis('off')
plt.title('Laplacian')
plt.imshow(LaplacianIGrad[:,:,::-1])

# plt.subplot(131)
# plt.axis('off')
# plt.title('Canny')
# plt.imshow(CannyIGrad, cmap='gray')
#
# plt.subplot(132)
# plt.axis('off')
# plt.title('Sobel')
# plt.imshow(SobelIGrad, cmap='gray')
#
# plt.subplot(133)
# plt.axis('off')
# plt.title('Laplacian')
# plt.imshow(LaplacianIGrad, cmap='gray')

plt.show()
