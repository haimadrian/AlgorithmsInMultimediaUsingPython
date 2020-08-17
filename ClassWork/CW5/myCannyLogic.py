__author__ = "Haim Adrian"

import numpy as np
from matplotlib import pyplot as plt
import cv2


def myGaussianBlur(image):
    if not isinstance(image, np.ndarray):
        print("myGaussianBlur: Not a tensor. Was: Image=", image.__class__)
        return None

    imgShape = image.shape
    if len(imgShape) == 2:
        gaussianMask = (1.0 / 273) * np.array([[1, 4, 7, 4, 1],
                                               [4, 16, 26, 16, 4],
                                               [7, 26, 41, 26, 7],
                                               [4, 16, 26, 16, 4],
                                               [1, 4, 7, 4, 1]],
                                              dtype=np.float64)

        img = np.float64(image.copy())
        cv2.filter2D(img, -1, gaussianMask)
    elif len(imgShape) == 3:
        b, g, r = cv2.split(image)
        img = cv2.merge((myGaussianBlur(b), myGaussianBlur(g), myGaussianBlur(r)))
    else:
        print("myGaussianBlur: Illegal image dimension. Length of shape can be 2 or 3 only")
        return None

    return img


def myGradient(image):
    if not isinstance(image, np.ndarray):
        print("myGradient: Not a tensor. Was: Image=", image.__class__)
        return None

    imgShape = image.shape
    if len(imgShape) == 2:
        img = np.float64(image.copy())
        sobelGradientXMask = np.array([[-1, 0, 1],
                                       [-2, 0, 2],
                                       [-1, 0, 1]],
                                      dtype=np.float64)
        sobelGradientYMask = np.array([[1, 2, 1],
                                       [0, 0, 0],
                                       [-1, -2, -1]],
                                      dtype=np.float64)

        print("myGradient: Applying Sobel Gradient X Mask")
        gradientX = cv2.filter2D(img, -1, sobelGradientXMask)

        print("myGradient: Applying Sobel Gradient Y Mask")
        gradientY = cv2.filter2D(img, -1, sobelGradientYMask)
        return gradientX, gradientY
    elif len(imgShape) == 3:
        b, g, r = cv2.split(image)
        bSobelX, bSobelY = myGradient(b)
        gSobelX, gSobelY = myGradient(g)
        rSobelX, rSobelY = myGradient(r)

        gradientX = cv2.merge((bSobelX, gSobelX, rSobelX))
        gradientY = cv2.merge((bSobelY, gSobelY, rSobelY))
        return gradientX, gradientY
    else:
        print("myGradient: Illegal image dimension. Length of shape can be 2 or 3 only")
        return None


def myPhase(gradientX, gradientY):
    if not isinstance(gradientX, np.ndarray) or not isinstance(gradientY, np.ndarray):
        print("myPhase: Not a tensor. Was: gradientX=", gradientX.__class__, "gradientY=", gradientY.__class__)
        return None

    gradientXShape = gradientX.shape
    gradientYShape = gradientY.shape
    if len(gradientXShape) == 2 and len(gradientYShape) == 2:
        print("myPhase: Calculating Intensity Gradient")
        intensityGradient = np.power((np.power(gradientX, 2) + np.power(gradientY, 2)), 0.5)
        # intensityGradient = intensityGradient * 255 / np.max(intensityGradient)

        print("myPhase: Calculating Phase")
        # phase = np.arctan(np.divide(gradientY, gradientX, out=np.zeros_like(gradientY), where=gradientX != 0))
        phase = np.arctan2(gradientY, gradientX)

        # Make it 0 to 180, instead of -90 to 90
        phase = phase * 180. / np.pi
        phase[phase < 0] += 180
    elif len(gradientXShape) == 3 and len(gradientYShape) == 3:
        bX, gX, rX = cv2.split(gradientX)
        bY, gY, rY = cv2.split(gradientY)

        intensityGradientB, phaseB = myPhase(bX, bY)
        intensityGradientG, phaseG = myPhase(gX, gY)
        intensityGradientR, phaseR = myPhase(rX, rY)

        intensityGradient = cv2.merge((intensityGradientB, intensityGradientG, intensityGradientR))
        phase = cv2.merge((phaseB, phaseG, phaseR))
    else:
        print("myPhase: Illegal dimension. Only 2D and 3D are supported. Was: gradientX=", gradientXShape, "gradientY=", gradientYShape)
        return None

    return intensityGradient, phase


def myNonMaximumSuppression(intensityGradient, phase):
    if not isinstance(intensityGradient, np.ndarray) or not isinstance(phase, np.ndarray):
        print("myNonMaximumSuppression: Not a tensor. Was: intensityGradient=", intensityGradient.__class__, "phase=", phase.__class__)
        return None

    intensityGradientShape = intensityGradient.shape
    phaseShape = phase.shape
    if len(intensityGradientShape) == 2 and len(phaseShape) == 2:
        nonMaxSuppress = np.zeros(intensityGradient.shape, dtype=np.int32)

        # First step: round angles
        phase[np.logical_or(phase < 22.5, phase >= 157.5)] = 0
        phase[np.logical_and(phase >= 22.5, phase < 67.5)] = 45
        phase[np.logical_and(phase >= 67.5, phase < 112.5)] = 90
        phase[np.logical_and(phase >= 112.5, phase < 57.5)] = 135

        # Second step: suppress inconsistent edges
        shape = intensityGradient.shape
        copy = intensityGradient.copy()
        copy -= np.min(copy)
        copy *= 255 / np.max(copy)
        padded = cv2.copyMakeBorder(copy, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
        for i in range(1, shape[0] + 1):
            for j in range(1, shape[1] + 1):
                currVal = phase[i - 1, j - 1]
                x = 0
                y = 0
                if currVal == 0:
                    x = padded[i, j + 1]  # East
                    y = padded[i, j - 1]  # West
                elif currVal == 90:
                    x = padded[i - 1, j]  # North
                    y = padded[i + 1, j]  # South
                elif currVal == 45:
                    x = padded[i - 1, j + 1]  # North-East
                    y = padded[i + 1, j - 1]  # South-West
                elif currVal == 135:
                    x = padded[i - 1, j - 1]  # North-West
                    y = padded[i + 1, j + 1]  # South-East

                # Copy the pixel only if it is in the right direction
                currR = padded[i, j]
                if (currR >= x or currR - x > -10) and (currR >= y or currR - y > -10):
                    nonMaxSuppress[i - 1, j - 1] = padded[i, j]
        return nonMaxSuppress
    elif len(intensityGradientShape) == 3 and len(phaseShape) == 3:
        intensityGradientB, intensityGradientG, intensityGradientR = cv2.split(intensityGradient)
        phaseB, phaseG, phaseR = cv2.split(phase)
        nonMaxSuppress = cv2.merge((myNonMaximumSuppression(intensityGradientB, phaseB),
                                    myNonMaximumSuppression(intensityGradientB, phaseG),
                                    myNonMaximumSuppression(intensityGradientB, phaseR)))
        return nonMaxSuppress
    else:
        print("myNonMaximumSuppression: Illegal dimension. Only 2D and 3D are supported. Was: intensityGradient=", intensityGradientShape, "phase=", phaseShape)
        return None


def myDoubleThreshold(intensityGradient, minThresh=0.25, maxThresh=0.5):
    if not isinstance(intensityGradient, np.ndarray):
        print("myDoubleThreshold: Not a tensor. Was: intensityGradient=", intensityGradient.__class__)
        return None

    strong = 255
    weak = 50

    intensityGradientShape = intensityGradient.shape
    if len(intensityGradientShape) == 2:
        result = np.zeros(intensityGradient.shape, dtype=np.int32)

        # Normalize intensity gradient to [0, 1]
        intensityGradient = np.float64(intensityGradient.copy())
        intensityGradient -= np.min(intensityGradient)
        intensityGradient /= np.max(intensityGradient)

        # strongRows, strongCols = np.where(intensityGradient > maxThresh)
        # weakRows, weakCols = np.where((intensityGradient >= minThresh) & (intensityGradient <= maxThresh))
        result[np.logical_and(intensityGradient >= minThresh, intensityGradient <= maxThresh)] = weak
        result[intensityGradient > maxThresh] = strong
        return result
    elif len(intensityGradient.shape) == 3:
        b, g, r = cv2.split(intensityGradient)
        bThresh = myDoubleThreshold(b, minThresh, maxThresh)
        gThresh = myDoubleThreshold(b, minThresh, maxThresh)
        rThresh = myDoubleThreshold(b, minThresh, maxThresh)
        result = cv2.merge((bThresh, gThresh, rThresh))
        return result, strong, weak
    else:
        print("myDoubleThreshold: Illegal dimension. Only 2D and 3D are supported. Was: intensityGradient=", intensityGradientShape)
        return None


def myHysteresis(intensityGradient, strong, weak):
    if len(intensityGradient.shape) == 3:
        b, g, r = cv2.split(intensityGradient)
        return cv2.merge((myHysteresis(b, strong, weak), myHysteresis(g, strong, weak), myHysteresis(r, strong, weak)))

    print("myHysteresis: Start. intensityGradient shape is:", intensityGradient.shape)
    visitedStrong = strong - 1

    def myHysteresisRec(mat, i, j, depth):
        shape = mat.shape

        # Make sure we are not out of bounds
        if 0 <= i < shape[0] and 0 <= j < shape[1]:
            if mat[i, j] == 0 or mat[i, j] == visitedStrong or (depth > 1 and mat[i, j] == strong):
                return mat[i, j]

            if depth > 750:
                return strong

            mat[i, j] = visitedStrong
            maxColor = visitedStrong
            maxColor = max(myHysteresisRec(mat, i - 1, j - 1, depth + 1), maxColor)
            maxColor = max(myHysteresisRec(mat, i - 1, j, depth + 1), maxColor)
            maxColor = max(myHysteresisRec(mat, i - 1, j + 1, depth + 1), maxColor)

            maxColor = max(myHysteresisRec(mat, i, j - 1, depth + 1), maxColor)
            maxColor = max(myHysteresisRec(mat, i, j + 1, depth + 1), maxColor)

            maxColor = max(myHysteresisRec(mat, i + 1, j - 1, depth + 1), maxColor)
            maxColor = max(myHysteresisRec(mat, i + 1, j, depth + 1), maxColor)
            maxColor = max(myHysteresisRec(mat, i + 1, j + 1, depth + 1), maxColor)
            mat[i, j] = maxColor
            return mat[i, j]
        return 0

    copy = np.int32(intensityGradient.copy())
    for i2 in range(copy.shape[0]):
        for j2 in range(copy.shape[1]):
            if copy[i2, j2] == strong:
                myHysteresisRec(copy, i2, j2, 1)

    # copy[copy == visitedStrong] = strong
    copy[copy == weak] = 0

    return copy


def normalizeImage(img):
    img = img - np.min(img)
    img = np.round(img * 255 / np.max(img))
    return np.uint8(img)


def plot(title, img, location):
    plt.subplot(location)
    plt.tight_layout(pad=2.0)
    plt.imshow(np.uint8(img[:, :, ::-1]))
    plt.title(title)
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
