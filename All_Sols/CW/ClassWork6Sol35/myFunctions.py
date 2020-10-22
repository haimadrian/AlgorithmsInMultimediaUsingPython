__author__ = 'Dmitry Patashov'

import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.io import wavfile as wfl


def GreenSqr(img, c, w):

    if img.__class__ != np.ndarray:
        return None

    img[c[0] - w: c[0] + w, c[1] - w: c[1] + w, 0:3:2] = 0

    return img

def QuadGreenSqr(img, s):

    if img.__class__ != np.ndarray:
        return None

    img[:,s,:] = np.array([0, 255, 0])

    return img

def ColorShift(img):

    if img.__class__ != np.ndarray:
        return None

    img[np.logical_and(img >= 75, img <=125)] *= 2

    return img

def myColorReplacement(img, read, write, amount, th):

    if img.__class__ != np.ndarray:
        return None

    myImg = img.copy()
    # ------------------------------------------------------------------
    # for m in range(read, read + amount):
    #     for n in range(myImg.shape[1]):
    #         if myImg[m,n,0] < th or myImg[m,n,2] < th:
    #             myImg[m - read + write, n, 1] = 255
    # ------------------------------------------------------------------
    myImg[write:write + amount, :, 1][np.logical_or(myImg[read:read + amount, :, 0] < th, myImg[read:read + amount, :, 2] < th)] = 255

    return myImg

def TwoLiner(img):
    if img.__class__ != np.ndarray:
        return None

    im = img.copy()
    D = im.shape
    th = np.int64(np.round(D[0] / 3.))
    wi = np.int64(np.round(D[0] / 30.))
    if len(D) != 3 or D[0] < 30:
        return None

    # ----------------------------------------------------------
    # for m in range(th - wi, th + wi + 1):
    #     for n in range(D[1]):
    #         im[m, n, 0] = 150
    #         im[m, n, 1] = 255
    #         im[m, n, 2] = 0
    # for m in range(2*th - wi, 2*th + wi + 1):
    #     for n in range(D[1]):
    #         im[m, n, 0] = 150
    #         im[m, n, 1] = 255
    #         im[m, n, 2] = 0
    # ----------------------------------------------------------

    im[list(range(th - wi, th + wi + 1)) + list(range(2 * th - wi, 2 * th + wi + 1)), :, :] = np.array([150, 255, 0])

    return im

def NoisySin(time, Ntype='n'):

    if time.__class__ != np.ndarray:
        return None
    if Ntype != 'n' and Ntype != 'g' and Ntype != 'u':
        return None
    elif Ntype == 'n' or Ntype == 'g':

        L = len(time)
        noise = np.random.normal(0, 0.1, L)

    else:

        L = len(time)
        noise = np.random.uniform(-0.2, 0.2, L)

    Sin = np.sin(time)
    Nsin = Sin + noise

    return Nsin, Sin, noise

def myMAF(signal, order=1):

    if signal.__class__ != np.ndarray:
        return None
    if order != np.int64(order) or order < 1:
        order = 1

    ps = np.concatenate((np.ones(order)*signal[0],signal,np.ones(order)*signal[-1]))
    filtSig = np.zeros(signal.shape)

    for k in range(len(signal)):
        filtSig[k] = np.mean(ps[k:k+2*order+1])

    return filtSig

def myMedFilt(signal, order=1):

    if signal.__class__ != np.ndarray:
        return None
    if order != np.int64(order) or order < 1:
        order = 1

    ps = np.concatenate((np.ones(order)*signal[0],signal,np.ones(order)*signal[-1]))
    filtSig = np.zeros(signal.shape)

    for k in range(len(signal)):
        filtSig[k] = np.median(ps[k:k+2*order+1])

    return filtSig


