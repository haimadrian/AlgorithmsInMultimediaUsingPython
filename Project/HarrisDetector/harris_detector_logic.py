__author__ = "Haim Adrian"

import cv2
import numpy as np
from matplotlib import pyplot as plt


def find_harris_corners(image, k, window_size, threshold):
    if not isinstance(image, np.ndarray):
        print("find_harris_corners: Not a tensor. Was: Image=", image.__class__)
        return None

    corner_list = []
    output_img = image.copy()
    gaussian_img = cv2.GaussianBlur(output_img, (5, 5), 3)

    offset = int(window_size / 2)
    x_range = gaussian_img.shape[0] - offset
    y_range = gaussian_img.shape[1] - offset

    dx, dy, dz = np.gradient(np.float64(gaussian_img))
    Ixx = dx ** 2
    Ixy = dy * dx
    Iyy = dy ** 2

    for x in range(offset, x_range):
        for y in range(offset, y_range):

            # Values of sliding window
            start_x = x - offset
            end_x = x + offset + 1
            start_y = y - offset
            end_y = y + offset + 1

            # The variable names are representative to
            # the variable of the Harris corner equation
            windowIxx = Ixx[start_x: end_x, start_y: end_y]
            windowIxy = Ixy[start_x: end_x, start_y: end_y]
            windowIyy = Iyy[start_x: end_x, start_y: end_y]

            # Sum of squares of intensities of partial derevatives
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            # Calculate determinant and trace of the matrix
            det = (Sxx * Syy) - (Sxy ** 2)
            trace = Sxx + Syy

            # Calculate r for Harris Corner equation
            r = det - k * (trace ** 2)

            if r > threshold:
                corner_list.append([x, y, r])
                # p1 = (x - window_size, y - window_size)
                # p2 = (x + window_size, y + window_size)
                center = (x, y)
                radius = 1
                color = (0, 255, 0)
                # cv2.rectangle(output_img, p1, p2, color)
                cv2.circle(output_img, center, radius, color)

    return corner_list, output_img


def plot(title, img, location):
    """
    This method created in order to wrap a sub plotting with tight layout

    Parameters
    ----------
    title : str or None
        The legend’s title. Default is no title (None).
    img : array_like, shape (n, m) or (n, m, 3) or (n, m, 4)
        The image to display
    location : int
        Represents the amount of rows, amount of columns and the plot number in the grid
    """
    plt.subplot(location)
    plt.tight_layout(pad=2.0)
    plt.imshow(np.uint8(img[:, :, ::-1]))
    plt.title(title)
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
