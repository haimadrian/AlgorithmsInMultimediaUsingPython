__author__ = 'Dmitry Patashov'

import numpy as np
from numpy import linalg as LA
import DataPreparation as dp
from matplotlib import pyplot as plt

# Load Data: --------------------------------------------------------------------------

ImageList = dp.LoadImageList()
TrainData,TrainLabels,TestData,TestLabels,ValidationData,ValidationLabels = dp.ReconstructData(ImageList)

print ('Data Loading Done')
# -------------------------------------------------------------------------------------

# Mean Removal: -----------------------------------------------------------------------

dataMean = np.mean(TrainData, axis=0)
centeredData = TrainData - dataMean

print ('Mean Removal Done')
# -------------------------------------------------------------------------------------

# Model Preparation: ------------------------------------------------------------------

CovMatSmall = centeredData.dot(centeredData.transpose())
eigenVals, eigenVecMatU = LA.eigh(CovMatSmall)
eigenVecMatW = np.dot(centeredData.transpose(), eigenVecMatU[:,::-1])
eigenVecMatV = eigenVecMatW / LA.norm(eigenVecMatW, axis = 0)

print ('Eigen Vectors Calculation Done')
# -------------------------------------------------------------------------------------

# Optimization of Eigen Faces: --------------------------------------------------------
print ('Begin Optimization')
progg = np.array((10,30,50,70,90), dtype=np.float64)

eigVecNum = eigenVecMatV.shape[1]
errList = []
for i in range(eigVecNum):
    eigenVecMatVk = eigenVecMatV[:, :eigVecNum - i]

    eigenFacesTr = TrainData.dot(eigenVecMatVk)
    eigenFacesTe = TestData.dot(eigenVecMatVk)

    TestAproxLabels = np.zeros((eigenFacesTe.shape[0], 1))
    for j in range(eigenFacesTe.shape[0]):
        diffVec = eigenFacesTr - eigenFacesTe[j, :]
        distVec = np.sqrt(np.sum(np.power(diffVec, 2), axis=1))
        TestAproxLabels[j, 0] = TrainLabels[np.argmin(distVec)]

    diffLabels = TestAproxLabels - TestLabels
    errVal = 100. * len(diffLabels[diffLabels != 0]) / TestLabels.shape[0]
    errList.append(errVal)

    cmpProg = i * 100.0 / eigVecNum
    if (cmpProg == progg).any():
        print ('\t Oprimization proccess', i * 100.0 / eigVecNum, '%')

errList.append(100.0)
successRateVec = 100 - np.asarray(errList[::-1])

print ('Optimization Done')
# -------------------------------------------------------------------------------------

# Classification and Result Validation: -----------------------------------------------

kVal = 130

eigenVecMatVk = eigenVecMatV[:, :kVal]

eigenFacesTr = TrainData.dot(eigenVecMatVk)
eigenFacesVa = ValidationData.dot(eigenVecMatVk)

ValAproxLabels = np.zeros((eigenFacesVa.shape[0], 1))
for j in range(eigenFacesVa.shape[0]):
    diffVec = eigenFacesTr - eigenFacesVa[j, :]
    distVec = np.sqrt(np.sum(np.power(diffVec, 2), 1))
    ValAproxLabels[j, 0] = TrainLabels[np.argmin(distVec)]

diffLabels = ValAproxLabels - ValidationLabels
errVal = 100. * len(diffLabels[diffLabels != 0]) / ValidationLabels.shape[0]
succRate = 100 - errVal

print ('Validation Classification Done')
# -------------------------------------------------------------------------------------

# Results Display: --------------------------------------------------------------------

plt.figure()

plt.axis([0, eigVecNum, 0, 100])
plt.yticks(np.arange(0, 100.1, 5.0))
plt.grid()

plt.plot(successRateVec)

plt.xlabel('Ammount of Eigenvectors K')
plt.ylabel('Detection Rate %')
mng = plt.get_current_fig_manager()
mng.window.showMaximized()

plt.show()

print ('\n\nEigenvectors ammount (k): ', kVal)
print ('Validation Success Rate: ', succRate, '%')

# -------------------------------------------------------------------------------------

# Visual Validation -------------------------------------------------------------------

print ('\nVisual Validation:')
print ('To exit visual validation enter any non numerical input')

Flag = True
while Flag:

    Mssg = 'Enter subject number 0-' + str(ValAproxLabels.shape[0] - 1) + ': '
    Inp = input(Mssg)
    Flag = dp.IsThisStringANumber(Inp)

    if Flag:
        TestNum = np.int64(Inp)
        if TestNum < 0:
            TestNum = 0
        elif TestNum > ValAproxLabels.shape[0] - 1:
            TestNum = ValAproxLabels.shape[0] - 1

        if TestNum % 2 == 0:
            ImgNum = 8
        else:
            ImgNum = 9

        aproxLabel = np.int64(ValAproxLabels[TestNum, 0])
        realLabel = np.int64(ValidationLabels[TestNum, 0])

        plt.figure()

        plt.subplot(121)
        plt.title('Input Subject:')
        plt.imshow(ImageList[aproxLabel][ImgNum], cmap='gray')

        plt.subplot(122)
        plt.title('Dtected as Subject:')
        plt.imshow(ImageList[realLabel][0], cmap='gray')

        mng = plt.get_current_fig_manager()
        mng.window.showMaximized()

        plt.show()

# -------------------------------------------------------------------------------------
