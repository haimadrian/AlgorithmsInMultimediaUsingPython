__author__ = "Haim Adrian"

import cv2
import matplotlib
from Functions import *

# Do it to see a new window when calling plt.show, and not within PyCharm.
matplotlib.use('TkAgg')


def ex1():
    img = cv2.imread('vegeta.jpg')
    GreenSqr(img, (img.shape[0] / 2, img.shape[1] / 2), 20)
    plt.figure('Assignment 1')
    plot("GreenSqr", img, 111)
    plt.subplots_adjust(0, 0, 1, 0.95, 0.05, 0.07)
    plt.show()


def ex2():
    img = cv2.imread('vegeta.jpg')
    QuadGreenSqr(img, [10, 11, 12, 20, 21, 30, 31, 50, 51, 150, 151, 200, 201, 202, 350, 351])
    plt.figure('Assignment 2')
    plot("QuadGreenSqr", img, 111)
    plt.subplots_adjust(0, 0, 1, 0.95, 0.05, 0.07)
    plt.show()


def ex3():
    img = cv2.imread('vegeta.jpg')
    copy = img.copy()
    ColorShift(copy)
    plt.figure('Assignment 3')
    plot("Original", img, 121)
    plot("ColorShift", copy, 122)
    plt.subplots_adjust(0, 0, 1, 0.95, 0.05, 0.07)
    plt.show()


def ex4():
    img = cv2.imread('vegeta.jpg')
    copy = myColorReplacement(img, 50, 100, 300, 170)
    copy2 = myColorReplacementLoop(img, 50, 100, 300, 170)
    plt.figure('Assignment 4')
    plot("Original", img, 131)
    plot("myColorReplacement", copy, 132)
    plot("myColorReplacementLoop", copy2, 133)
    plt.subplots_adjust(0, 0, 1, 0.95, 0.05, 0.07)
    plt.show()


def ex5():
    img = cv2.imread('vegeta.jpg')
    copy = TwoLiner(img)
    copy2 = TwoLinerLoop(img)
    plt.figure('Assignment 5')
    plot("Original", img, 131)
    plot("TwoLiner", copy, 132)
    plot("TwoLinerLoop", copy2, 133)
    plt.subplots_adjust(0, 0, 1, 0.95, 0.05, 0.07)
    plt.show()


def ex6():
    time = np.arange(0, 2*np.pi, 0.01)
    noisySin, sinAmplitude, noise = NoisySin(time)
    noisySinU, sinAmplitudeU, noiseU = NoisySin(time, 'u')

    plt.figure('Assignment 6')
    plt.subplot(221)
    plt.plot(time, sinAmplitude, label='Sine Wave')
    plt.plot(time, noise, label='Gauss Noise')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplot(223)
    plt.plot(time, noisySin, label='Noisy Sine Wave (G|N)')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplot(222)
    plt.plot(time, sinAmplitudeU, label='Sine Wave')
    plt.plot(time, noiseU, label='Uniform Noise')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplot(224)
    plt.plot(time, noisySinU, label='Noisy Sine Wave (U)')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplots_adjust(0.1, 0.1, 0.9, 0.9, 0.1, 0.3)
    plt.show()


def ex7():
    time = np.arange(0, 2*np.pi, 0.01)
    noisySin, sinAmplitude, noise = NoisySin(time)

    mafForNoisySin = myMAF(noisySin, 10)

    plt.figure('Assignment 7')
    plt.subplot(211)
    plt.plot(time, noisySin, label='Noisy Signal')
    plt.plot(time, mafForNoisySin, label='Filtered Signal')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplot(212)
    plt.plot(time, sinAmplitude, label='Sine Wave')
    plt.plot(time, mafForNoisySin, label='Filtered Signal')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplots_adjust(0.1, 0.1, 0.9, 0.9, 0.1, 0.3)
    plt.show()


def ex8():
    time = np.arange(0, 2*np.pi, 0.01)
    noisySin, sinAmplitude, noise = NoisySin(time, 'u')

    medForNoisySin = myMedFilt(noisySin, 30)

    plt.figure('Assignment 8')
    plt.subplot(211)
    plt.plot(time, noisySin, label='Noisy Signal')
    plt.plot(time, medForNoisySin, label='Filtered Signal')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplot(212)
    plt.plot(time, sinAmplitude, label='Sine Wave')
    plt.plot(time, medForNoisySin, label='Filtered Signal')
    plt.legend()
    plt.axhline(y=0, color='k')

    plt.subplots_adjust(0.1, 0.1, 0.9, 0.9, 0.1, 0.3)
    plt.show()


def ex9():
    sampling_rate, stereo, mono, mixed = mix('rain.wav', 'Walking.wav')
    time = np.linspace(0, len(mixed) / sampling_rate, num=len(mixed))

    plt.figure('Assignment 9')
    plt.subplot(221)
    plt.plot(time, mono)
    plt.title('Walking.wav (mono)')
    plt.axhline(y=0, color='k')

    plt.subplot(222)
    plt.plot(time, np.mean(stereo, 1))
    plt.title('rain.wav (mono)')
    plt.axhline(y=0, color='k')

    plt.subplot(212)
    plt.plot(time, np.mean(mixed, 1))
    plt.title('mixed.wav (mono)')
    plt.axhline(y=0, color='k')

    plt.subplots_adjust(0.1, 0.1, 0.9, 0.9, 0.2, 0.3)
    plt.show()


ex9()
