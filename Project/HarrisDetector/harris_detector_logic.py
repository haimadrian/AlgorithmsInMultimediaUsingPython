__author__ = "Haim Adrian"

import cv2
import numpy as np


def log(consumer, *message):
    text = ' '.join(message)
    if consumer is not None:
        consumer(text)

    print(text)


def do_progress(consumer, current_progress, step):
    if consumer is not None:
        current_progress += step
        consumer(current_progress)

    return current_progress


# I have created this method to compare matrices between py3.5 and py3.7 in order to find a bug I had in py3.5,
# where I used a uint8 matrix rather than float64 and had overflows occurred in py3.5
def dump_matrix_to_disk(mat, file_name):
    with open(file_name, 'wb') as f:
        f.write(str.encode(str(mat.shape)))
        f.write(str.encode('\n'))
        for line in mat:
            np.savetxt(f, line, fmt='%.2f')


def find_harris_corners(image, k, window_size, console_consumer=None, progress_consumer=None, progress=0, max_progress=99):
    """
    Harris Corner Detector algorithm implementation.
    Harris detector responses are the CRF(x, y) values from the equation: CRF = det(M) − k*(tr(M)**2) (Corner Response Function)
    where det(M) = Lambda1*Lambda2, which is the value of the determinant, and tr(M) = Lambda1+Lambda2, which is the trace
    of the determinant. (Lambda1, Lambda2 = eigen values).
    When the CRF value of the pixel point is greater than the given threshold, it is determined that the target point is a corner point.
    :param image: Input single-channel 8-bit or floating-point image.
    :param k: Harris detector free parameter in the equation.
    :param window_size: Neighborhood size.
    :param console_consumer: Used for logging purposes. (Passing step updates to a listener)
    :param progress_consumer: A lambda / function to handle progress updates
    :param progress: Starting value of the progress, to show progress relative to this value
    :param max_progress: Ending value of the progress, to show progress until this value
    :return: Image to store the Harris detector responses. It has the same size as source image. dst(x,y) = detM(x,y) − k*(trM(x,y)**2)
    Corners in the image can be found as the local maxima of this response map.
    """
    if not isinstance(image, np.ndarray):
        log(console_consumer, "find_harris_corners: Not a tensor. Was: Image=", image.__class__)
        return None

    if image.ndim not in [2, 3]:
        log(console_consumer, 'find_harris_corners: Illegal image dimension. Image N-dimension can be 2 or 3 only. Was:', image.ndim)
        return None

    harris_responses = np.zeros((image.shape[0], image.shape[1]), dtype=np.float64)

    if image.ndim == 3:
        twoD = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        twoD = image

    offset = int(window_size / 2)

    # Pad the image so we can calculate Harris score for the whole image
    # Use Copy Padding so we will not accidentally invent corners with a constant padding of 0's
    # From now on, go ahead as float64. Otherwise this won't work in py3.5 (It does work in 3.7 however)
    padded = np.float64(cv2.copyMakeBorder(twoD, offset, offset, offset, offset, cv2.BORDER_REPLICATE))

    # For 2D array, so the result of gradient is two arrays ordered by axis
    dy, dx = np.gradient(padded)

    # Compute products of derivatives at every pixel
    Ixx = dx ** 2
    Ixy = dx * dy
    Iyy = dy ** 2

    # Calculate step size in the area we have to progress in a progressbar
    progress_steps_left = max_progress - progress
    progress_step = progress_steps_left / image.shape[0]
    for x in range(offset, padded.shape[0] - offset):
        for y in range(offset, padded.shape[1] - offset):
            # The window according to the Harris Equation
            window_Ixx = Ixx[x - offset: x + offset + 1, y - offset: y + offset + 1]
            window_Ixy = Ixy[x - offset: x + offset + 1, y - offset: y + offset + 1]
            window_Iyy = Iyy[x - offset: x + offset + 1, y - offset: y + offset + 1]

            # Sum the squares in the sliding window.
            # Here is the M = SUM_for-each-x-y(window(x, y)[[Ixx, Ixy], [Ixy, Iyy]]
            sum_xx = window_Ixx.sum()
            sum_xy = window_Ixy.sum()
            sum_yy = window_Iyy.sum()

            # Calculate determinant and trace for the sum of squares matrix (M)
            detM = (sum_xx * sum_yy) - (sum_xy * sum_xy)  # Multiply main diagonal, minus multiplication of secondary diagonal
            traceM = sum_xx + sum_yy  # Main diagonal

            # Calculate corner_response_function for Harris Corner equation
            corner_response_function = detM - k * (traceM ** 2)

            harris_responses[x - offset, y - offset] = corner_response_function
        progress = do_progress(progress_consumer, progress, progress_step)

    return harris_responses
