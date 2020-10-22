import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Cat.jpg')
b,g,r = cv2.split(img)

PixelsPerWave = 10

WaveSize = 2.0 * np.pi/PixelsPerWave
m,n = g.shape
cm = np.int(m/2)
cn = np.int(n/2)

WaveMat = np.zeros([m,n])
for i in range(m):
    for j in range(n):
        WaveMat[i][j] = np.sin(np.sqrt((cm - i)**2 + (j - cn)**2)*WaveSize)

ImMat = ((WaveMat + 1.0)/2.0)
WaveB = np.float64(b)*ImMat
WaveG = np.float64(g)*ImMat
WaveR = np.float64(r)*ImMat
WaveImage = cv2.merge((np.uint8(WaveR),np.uint8(WaveG),np.uint8(WaveB)))

BFreq = np.fft.fftshift(np.fft.fft(b)) * ImMat
GFreq = np.fft.fftshift(np.fft.fft(g)) * ImMat
RFreq = np.fft.fftshift(np.fft.fft(r)) * ImMat

WeveFreqB = np.absolute(np.fft.ifft(np.fft.ifftshift(BFreq)))
WeveFreqG = np.absolute(np.fft.ifft(np.fft.ifftshift(GFreq)))
WeveFreqR = np.absolute(np.fft.ifft(np.fft.ifftshift(RFreq)))

WaveFreqImage = cv2.merge((np.uint8(WeveFreqR),np.uint8(WeveFreqG),np.uint8(WeveFreqB)))

plt.figure(1)
plt.subplot(222)
plt.title('2D Sin')
plt.imshow(np.uint8(ImMat*255), cmap='Greys_r')
plt.subplot(221)
plt.title('Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(223)
plt.title('Product Image*Sin')
plt.imshow(WaveImage)
plt.subplot(224)
plt.title('Product ImFrequency*Sin')
plt.imshow(WaveFreqImage)
plt.show()
