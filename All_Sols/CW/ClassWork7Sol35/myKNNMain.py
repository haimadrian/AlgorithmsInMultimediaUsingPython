__author__ = 'Dmitry Patashov'

import pandas as pd
import numpy as np
import os
import myKNNLogic as kl

dataNum = 1  # 1-4
k = 7

currDir = os.getcwd()
knnDataAdd = currDir + '\\KNN Data\\'
dataName = 'Data' + str(dataNum) + '.xlsx'
xl = pd.ExcelFile(knnDataAdd+dataName)
df = xl.parse("Sheet1")

DataMat = np.asarray(df)

data = DataMat[:,0:3]
newData = DataMat[:,3:]

# Plot the samples in a different color for each type

kl.PlotData(data)

# Use the KNN algorithm to classify the NewSamples.

labeledData = kl.myKNN(k, data, newData)

kl.PlotData(labeledData)

# Test

kl.PlotData(data, 50, 0, 1, 'k = ' + str(k))
kl.PlotData(labeledData, 10, 1, 0)

