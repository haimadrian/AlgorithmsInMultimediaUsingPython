__author__ = 'Dmitry Patashov'

from myFunctions import *

qn = 1

if qn == 1:
    myGradDescent()

else:

    TrainDataMat, TrainLabelVec, TestDataMat, TestLabelVec = LoadMnistData()

    num1, num2 = 0., 1.
    bTrainDataMat, bTrainLabelVec, bTestDataMat, bTestLabelVec = BinarizeData(TrainDataMat, TrainLabelVec, TestDataMat, TestLabelVec, num1, num2)

    W = myLogisticRegression(bTrainDataMat, bTrainLabelVec)

    ApproximateLabel = myLogisticClassification(bTestDataMat, W)

    acc = 100 * np.sum(np.abs(ApproximateLabel - bTestLabelVec)) / len(bTestLabelVec)

    print (acc)


