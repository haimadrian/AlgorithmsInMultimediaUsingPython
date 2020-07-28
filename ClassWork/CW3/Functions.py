import numpy as np
import cv2
from matplotlib import pyplot as plt


# Assignment 1
def showImageTwice(imgName):
    if imgName.__class__ != "".__class__:
        return None

    img = cv2.imread(imgName)
    cv2.imshow(imgName, img)

    plt.figure(imgName)
    plt.imshow(img[:, :, ::-1])
    plt.show()


def validateImage(img):
    if not isinstance(img, np.ndarray):
        return None

    dim = img.shape
    if len(dim) < 2 or len(dim) > 3:
        return None

    if len(dim) == 2:
        img = cv2.merge((img, img, img))

    return img


# Assignment 2
def myBGR2RGB(bgr):
    bgr = validateImage(bgr)
    if bgr is None:
        return None

    return bgr[:, :, ::-1]


# Assignment 3
def splitRGB(imgName='img4.jpeg'):
    if imgName.__class__ != ''.__class__:
        return None

    img = cv2.imread(imgName)
    imgRGB = myBGR2RGB(img)

    imgR = imgRGB.copy()
    imgR[:, :, 1:3] = 0
    imgG = imgRGB.copy()
    imgG[:, :, 0] = 0
    imgG[:, :, 2] = 0
    imgB = imgRGB.copy()
    imgB[:, :, 0:2] = 0

    plt.figure('EX3')
    plt.subplot(131)
    plt.imshow(imgR)
    plt.axis('off')
    plt.subplot(132)
    plt.imshow(imgG)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(imgB)
    plt.axis('off')
    plt.show()

    bTranspose = imgRGB.copy()[:, :, 2]
    bTranspose = bTranspose.transpose()
    imgBTranspose = imgRGB.copy()
    imgBTranspose[:, :, 2] = bTranspose

    gUpsideDown = imgRGB.copy()[:, :, 1]
    gUpsideDown = gUpsideDown[::-1, :]
    imgGUpsideDown = imgRGB.copy()
    imgGUpsideDown[:, :, 1] = gUpsideDown
    plt.figure('EX3.2')
    plt.subplot(121)
    plt.imshow(imgBTranspose)
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(imgGUpsideDown)
    plt.axis('off')
    plt.show()


# Assignment 4
def drawGreenHorizontalLine(img):
    img = validateImage(img)
    if img is None:
        return None
    dim = img.shape

    middle = int(dim[0] / 2)
    x1, y1 = 0, middle
    x2, y2 = dim[1], middle
    image = img.copy()

    line_thickness = 2
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=line_thickness)

    return image


# Assignment 5
def drawRedDiagonalLine(img):
    img = validateImage(img)
    if img is None:
        return None
    dim = img.shape

    x1, y1 = 0, 0
    x2, y2 = dim[1], dim[0]
    image = img.copy()

    line_thickness = 2
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), thickness=line_thickness)

    return image


# Assignment 6
def drawBlueSquare(img):
    img = validateImage(img)
    if img is None:
        return None
    dim = img.shape

    middleVertical = int(dim[0] / 2)
    middleHorizontal = int(dim[1] / 2)
    width = int(middleVertical / 2)
    x1, y1 = middleHorizontal - width, middleVertical - width
    x2, y2 = middleHorizontal + width, middleVertical + width
    image = img.copy()

    line_thickness = 2
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), thickness=line_thickness)

    return image


# Assignment 7
def drawPurpleCircle(img):
    img = validateImage(img)
    if img is None:
        return None
    dim = img.shape

    image = img.copy()
    line_thickness = 2
    center = (int(dim[0] / 2), int(dim[1] / 2))
    radius = int(dim[0] / 4)
    cv2.circle(image, center, radius, [128, 0, 128], thickness=line_thickness)

    return image


# Assignment 8
def drawTriangle(img):
    img = validateImage(img)
    if img is None:
        return None
    dim = img.shape

    x1, y1 = int(dim[1] / 2), int(dim[0] / 3)
    x2, y2 = int(dim[1] / 3), dim[0] - int(dim[0] / 3)
    x3, y3 = dim[1] - int(dim[1] / 3), dim[0] - int(dim[0] / 3)
    image = img.copy()

    line_thickness = 3
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), thickness=line_thickness)
    cv2.line(image, (x1, y1), (x3, y3), (255, 0, 0), thickness=line_thickness)
    cv2.line(image, (x2, y2), (x3, y3), (0, 255, 0), thickness=line_thickness)

    return image


# Assignment 9
def drawGrayscale(imgName='img1.jpg'):
    if imgName.__class__ != ''.__class__:
        return None

    img = cv2.imread(imgName)
    imageMinus = img.copy()
    imagePlus = img.copy()

    # Convert to float64 so we will be able to have negative values, below uint8
    imageMinus = np.float64(imageMinus) - 50
    imageMinus[imageMinus < 0] = 0
    imageMinus = np.uint8(imageMinus)
    imagePlus = np.float64(imagePlus) + 50
    imagePlus[imagePlus > 255] = 255
    imagePlus = np.uint8(imagePlus)

    plt.figure('Gray Scale')
    plt.subplot(231)
    plt.imshow(cv2.cvtColor(imageMinus, cv2.COLOR_BGR2GRAY), cmap="gray")
    plt.axis('off')
    plt.title('image - 50')
    plt.subplot(232)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cmap="gray")
    plt.axis('off')
    plt.title('image')
    plt.subplot(233)
    plt.imshow(cv2.cvtColor(imagePlus, cv2.COLOR_BGR2GRAY), cmap="gray")
    plt.axis('off')
    plt.title('image + 50')
    plt.subplot(212)
    plt.imshow(myBGR2RGB(img))
    plt.axis('off')
    plt.title('original image')
    plt.show()


# Assignment 10
def myZeroPadding(img, padSize):
    if not isinstance(img, np.ndarray) or not isinstance(padSize, int):
        return None

    # Zero Padding
    return cv2.copyMakeBorder(img, padSize, padSize, padSize, padSize, cv2.BORDER_CONSTANT, value=[0, 0, 0])


# Assignment 11
def myExtendedPadding(img, padSize):
    if not isinstance(img, np.ndarray) or not isinstance(padSize, int):
        return None

    # Extended Padding
    return cv2.copyMakeBorder(img, padSize, padSize, padSize, padSize, cv2.BORDER_REPLICATE)


# Assignment 12
def fuck(img):
    img = validateImage(img)
    if img is None:
        return None

    def GradientEdgeDetector(myImage):
        dy, dx = np.gradient(np.float64(myImage))

        newImg = (dy ** 2 + dx ** 2) ** 0.5
        newImg = newImg - np.min(newImg)
        newImg = np.round(newImg * 255 / np.max(newImg))

        return np.uint8(newImg)

    b, g, r = cv2.split(img)
    Pb = GradientEdgeDetector(b)
    Pg = GradientEdgeDetector(g)
    Pr = GradientEdgeDetector(r)

    return cv2.merge((Pb, Pg, Pr))
