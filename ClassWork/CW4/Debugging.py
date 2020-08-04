import numpy as np
import cv2
from matplotlib import pyplot as plt


def normalizeImage(img):
    img = img - np.min(img)
    img = np.round(img * 255 / np.max(img))
    return np.uint8(img)


def doSomething():
    img = cv2.imread('Cat.jpg')
    b, g, r = cv2.split(img)

    PixelsPerWave = 10

    WaveSize = 2.0 * np.pi / PixelsPerWave
    m, n = g.shape
    cm = np.int(m / 2)
    cn = np.int(n / 2)

    WaveMat = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            WaveMat[i, j] = np.sin(np.sqrt((cm - i) ** 2 + (j - cn) ** 2) * WaveSize)

    ImMat = ((WaveMat + 1.0) / 2.0)
    WaveB = np.float64(b) * ImMat
    WaveG = np.float64(g) * ImMat
    WaveR = np.float64(r) * ImMat
    WaveImage = cv2.merge((WaveR, WaveG, WaveB))

    BFreq = np.fft.fftshift(np.fft.fft(b)) * ImMat
    GFreq = np.fft.fftshift(np.fft.fft(g)) * ImMat
    RFreq = np.fft.fftshift(np.fft.fft(r)) * ImMat

    WeveFreqB = np.absolute(np.fft.ifft(np.fft.ifftshift(BFreq)))
    WeveFreqG = np.absolute(np.fft.ifft(np.fft.ifftshift(GFreq)))
    WeveFreqR = np.absolute(np.fft.ifft(np.fft.ifftshift(RFreq)))

    WaveFreqImage = cv2.merge((normalizeImage(WeveFreqR), normalizeImage(WeveFreqG), normalizeImage(WeveFreqB)))

    plt.figure(1)
    plt.subplot(222)
    plt.title('2D Sin')
    plt.imshow(normalizeImage(ImMat * 255))
    plt.axis('off')
    plt.subplot(221)
    plt.title('Image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.subplot(223)
    plt.title('Product Image*Sin')
    plt.imshow(normalizeImage(WaveImage))
    plt.axis('off')
    plt.subplot(224)
    plt.title('Product ImFrequency*Sin')
    plt.imshow(WaveFreqImage)
    plt.axis('off')
    plt.show()
