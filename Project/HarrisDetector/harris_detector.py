__author__ = "Haim Adrian"

from timeit import default_timer as timer
from harris_detector_logic import *


def corners_and_line_intersection_detector(image_path, console_consumer=None, is_using_canny=False):
    """
    Main entry point to the Harris Detector algorithm
    We call this method from main frame in order to open an image, detect corners in it, and return both the image and
    a copy of the image with the corners marked out
    :param image_path: Path of the image to read
    :param console_consumer: A lambda / function to handle status updates
    :param is_using_canny: Whether we should detect edges using Canny Edge Detection before Harris Detector, or not
    :return: image, image_with_marks
    """
    start = timer()
    img = cv2.imread(image_path)

    success = False

    if img is None:
        log(console_consumer, 'Unable to open image:', image_path)
        processed_image = None
    else:
        k = 0.04
        window_size = 5
        threshold = 10000.00

        image = img.copy()
        if is_using_canny:
            log(console_consumer, 'Running Canny Edge Detection...')
            image = cv2.Canny(image, 0.5, 200)
            image = cv2.merge((image, image, image))

        log(console_consumer, 'Detecting corners...')
        corner_list, processed_image = find_harris_corners(image, k, window_size, threshold)

        if processed_image is None:
            log(console_consumer, 'Error has occurred while detecting corners. Result was None')
        else:
            success = True

    time_took = timer() - start
    log(console_consumer, 'Corners detection ended in %.2f seconds. Result:' % time_took, 'Success' if success else 'Fail')
    return img, processed_image
