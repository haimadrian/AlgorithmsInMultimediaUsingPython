__author__ = "Haim Adrian"


import scipy.ndimage as ndimage
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile


def GreenSqr(image, center, width):
    if not isinstance(image, np.ndarray):
        print("GreenSqr: Not a tensor. Was: Image=", image.__class__)
        return None

    if not isinstance(center, tuple) or len(center) != 2:
        print("GreenSqr: Center point should contain two values (x, y). Was: center=", center)
        return None

    if not isinstance(width, int):
        print("GreenSqr: Width should be a number. Was: width=", width.__class__)
        return None

    if len(image.shape) == 2:
        w = 2 * width + 1
        image[center[0] - w: center[0] + w, center[1] - w: center[1] + w] = 255
    elif len(image.shape) == 3:
        w = 2 * width + 1
        image[int(center[0] - w): int(center[0] + w), int(center[1] - w): int(center[1] + w)] = 0, 255, 0
    else:
        print("GreenSqr: Unsupported shape. Was:", image.shape)
        return None


def QuadGreenSqr(image, rows):
    if not isinstance(image, np.ndarray):
        print("QuadGreenSqr: Not a tensor. Was: Image=", image.__class__)
        return None

    if not isinstance(rows, list):
        print("QuadGreenSqr: Rows should be a list. Was: rows=", rows.__class__)
        return None

    image[:, rows] = 0, 255, 0


def ColorShift(image):
    if not isinstance(image, np.ndarray):
        print("ColorShift: Not a tensor. Was: Image=", image.__class__)
        return None

    image[np.logical_and(image >= 75, image <= 125)] *= 2


def myColorReplacementLoop(img, read, write, amount, th):
    if img.__class__ != np.ndarray:
        return None

    myImg = img.copy()

    for m in range(read, read + amount):
        for n in range(myImg.shape[1]):
            if myImg[m, n, 0] < th or myImg[m, n, 2] < th:
                myImg[m - read + write, n, 1] = 255

    return myImg


def myColorReplacement(img, read, write, amount, th):
    if img.__class__ != np.ndarray:
        return None

    myImg = img.copy()
    myImg[write: write + amount, :, 1][np.logical_or(myImg[read: read + amount, :, 0] < th, myImg[read: read + amount, :, 2] < th)] = 255

    return myImg


def TwoLinerLoop(img):
    if img.__class__ != np.ndarray:
        return None

    im = img.copy()
    D = im.shape
    th = np.int64(np.round(D[0]/3.))
    wi = np.int64(np.round(D[0]/30.))
    if len(D) != 3 or D[0] < 30:
        return None

    for m in range(th - wi, th + wi + 1):
        for n in range(D[1]):
            im[m, n, 0] = 150
            im[m, n, 1] = 255
            im[m, n, 2] = 0
    for m in range(2*th - wi, 2*th + wi + 1):
        for n in range(D[1]):
            im[m, n, 0] = 150
            im[m, n, 1] = 255
            im[m, n, 2] = 0

    return im


def TwoLiner(img):
    if img.__class__ != np.ndarray:
        return None

    im = img.copy()
    D = im.shape
    th = np.int64(np.round(D[0]/3.))
    wi = np.int64(np.round(D[0]/30.))
    if len(D) != 3 or D[0] < 30:
        return None

    im[(list(range(th - wi, th + wi + 1)) + list(range(th*2 - wi, th*2 + wi + 1))), :] = 150, 255, 0

    return im


def NoisySin(time, nType='g'):
    amplitude = np.sin(time)

    if nType == 'u':
        # Uniform distribution parameters
        low = -0.25
        high = 0.25
        noise = np.random.uniform(low, high, len(amplitude))
    else:
        # Gaussian distribution parameters
        mean = 0  # y = 0
        sigma = 1/8.0  # width (spread)
        noise = np.random.normal(mean, sigma, len(amplitude))

    noisy = amplitude + noise

    return noisy, amplitude, noise


def myMAF(signal, order=1):
    if not isinstance(signal, np.ndarray):
        print("myMAF: Not a tensor. Was: signal=", signal.__class__)
        return None

    if len(signal.shape) != 1:
        print("myMAF: Unsupported shape:", signal.shape)
        return None

    if order < 1:
        order = 1

    order = int(np.round(order))

    # padded = np.pad(signal, (order, order), 'edge')
    mafFilter = np.ones(2*order + 1) / (2.0*order + 1.0)
    return ndimage.convolve(signal, mafFilter)


def myMedFilt(signal, order=1):
    if not isinstance(signal, np.ndarray):
        print("myMedFilt: Not a tensor. Was: signal=", signal.__class__)
        return None

    if len(signal.shape) != 1:
        print("myMedFilt: Unsupported shape:", signal.shape)
        return None

    if order < 1:
        order = 1

    order = int(np.round(order))
    padded = np.pad(signal, (order, order), 'edge')  # Extend Padding
    result = np.zeros(len(signal))

    for i in range(order, len(signal) + order):
        result[i - order] = np.median(padded[i - order: i + order])

    return result


def mix(stereo_audio_path, mono_audio_path):
    # Stereo has two columns where column 0 is the left channel and column 1 is the right channel
    # The rows in stereo audio represent the signal
    sampling_rate1, stereo_data = wavfile.read(stereo_audio_path)
    sampling_rate2, mono_data = wavfile.read(mono_audio_path)

    if len(stereo_data.shape) != 2:
        print('mix: Stereo file had unexpected shape. Was:', stereo_data.shape)
        return None

    if len(mono_data.shape) != 1:
        print('mix: Mono file had unexpected shape. Was:', mono_data.shape)
        return None

    # Adjust to the same length
    minLen = np.min([stereo_data.shape[0], len(mono_data)])
    data1 = np.float64(stereo_data[: minLen, :])
    data2 = np.float64(mono_data[:minLen])

    # We use these for normalizing the signals
    maxOfMaxs = np.max([np.max(data1[0]), np.max(data1[1]), np.max(data2)])
    if maxOfMaxs < 0:
        maxOfMaxs *= -1

    minOfMins = np.min([np.min(data1[0]), np.min(data1[1]), np.min(data2)])
    if minOfMins > 0:
        minOfMins *= -1

    # Normalize the signals
    data2[data2 >= 0] *= maxOfMaxs / np.max(data2)
    data1[:, 0][data1[:, 0] >= 0] *= maxOfMaxs / np.max(data1[:, 0])
    data1[:, 1][data1[:, 1] >= 0] *= maxOfMaxs / np.max(data1[:, 1])
    data2[data2 < 0] *= minOfMins / np.min(data2)
    data1[:, 0][data1[:, 0] < 0] *= minOfMins / np.min(data1[:, 0])
    data1[:, 1][data1[:, 1] < 0] *= minOfMins / np.min(data1[:, 1])

    # Add the mono sound into the stereo one
    result = np.zeros((minLen, 2), dtype=np.float64)
    result[:, 0] += data1[:, 0]
    result[:, 0] += data2
    result[:, 1] += data1[:, 0]
    result[:, 1] += data2

    # Make sure we do not exceed in16
    result = np.round(result)
    result[result > 32767] = 32767
    result[result < -32768] = -32768
    result = np.int16(result)

    wavfile.write('Mixed.wav', sampling_rate1, result)

    return sampling_rate1, stereo_data[: minLen, :], mono_data[:minLen], result


def plot(title, img, location):
    plt.subplot(location)
    plt.tight_layout(pad=2.0)
    plt.imshow(np.uint8(img[:, :, ::-1]))
    plt.title(title)
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
