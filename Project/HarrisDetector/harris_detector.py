__author__ = "Haim Adrian"

from timeit import default_timer as timer
from harris_detector_logic import *


def corners_and_line_intersection_detector(image_path, console_consumer=None, is_using_canny=False, is_applying_gauss=False,
                                           is_using_rect=True, dilate_size=20):
    """
    Main entry point to the Harris Detector algorithm
    We call this method from main frame in order to open an image, detect corners in it, and return both the image and
    a copy of the image with the corners marked out
    :param image_path: Path of the image to read
    :param console_consumer: A lambda / function to handle status updates
    :param is_using_canny: Whether we should detect edges using Canny Edge Detection before Harris Detector, or not
    :param is_applying_gauss: Whether to apply Gaussian Blur before executing Harris Corner Detector
    :param is_using_rect: Whether mark corners using a rectangle or not. (If not, we mark corners using dots)
    :param dilate_size: Rectangle size
    :return: image, image_with_marks
    """
    start = timer()
    img = cv2.imread(image_path)

    success = False

    if img is None:
        log(console_consumer, 'Unable to open image:', image_path)
        image = None
    else:
        image = img.copy()
        if is_using_canny:
            log(console_consumer, 'Running Canny Edge Detection...')
            image = cv2.Canny(image, 100, 200)  # yields 2D

        if is_applying_gauss:
            log(console_consumer, 'Applying Gaussian Blur...')
            image = apply_gaussian_blur(image)  # yields either 3D or 2D, depends on the image

        log(console_consumer, 'Detecting corners...')
        harris_scores = find_harris_corners(image, 0.04, 5, console_consumer)

        if harris_scores is None:
            log(console_consumer, 'Error has occurred while detecting corners. Result was None')
            image = None
        else:
            success = True
            image = img.copy()
            if image.ndim == 2:
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            # Mark the corners
            if is_using_rect:
                mark_corners_with_rect(image, harris_scores, dilate_size)
            else:
                # Mark with dots
                harris_scores = cv2.dilate(harris_scores, None)
                image[harris_scores > 0.01 * harris_scores.max()] = (0, 255, 0)

    time_took = timer() - start
    log(console_consumer, 'Corners detection ended in %.2f seconds. Result:' % time_took, 'Success' if success else 'Fail')
    return img, image


def apply_gaussian_blur(image):
    if image.ndim == 2:
        gaussian_img = cv2.GaussianBlur(image, (5, 5), 0)
    elif image.ndim == 3:
        b, g, r = cv2.split(image)
        gaussian_img = cv2.merge((cv2.GaussianBlur(b, (5, 5), 0), cv2.GaussianBlur(g, (5, 5), 0), cv2.GaussianBlur(r, (5, 5), 0)))
    else:
        gaussian_img = image

    return gaussian_img


def mark_corners_with_rect(image, harris_scores, dilate_size):
    """
    A helper method we use to make the marks of corner as rectangles rather than single pixels.
    Use a blank image (black), then light up the pixels that have been found by Harris Detector
    This way we create a clear image, without any noise, and then we can safely dilate the image to make the
    lights thicker, find the contours and then paint rectangles using the contours
    :param image: The image to paint the marks on
    :param harris_scores: The R values (scores) from Harris Detector algorithm
    :param dilate_size: The size to use as kernel for cv2.dilate (Affect rectangle size)
    :return: None
    """
    helper_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    # Threshold for an optimal value, it may vary depending on the image.
    helper_image[harris_scores > 0.01 * harris_scores.max()] = 255
    cv2.threshold(helper_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU, helper_image)

    # Make the pixels thicker (marking the corners)
    kernel_size = dilate_size
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    helper_image = cv2.dilate(helper_image, kernel, iterations=1)

    # Find all contours so we can make rectangles out of them
    contours, hierarchy = cv2.findContours(helper_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # Get the bounding rect
        left, top, width, height = cv2.boundingRect(c)

        # Draw a green rectangle to visualize the bounding rect
        cv2.rectangle(image, (left, top), (left + width, top + height), (0, 255, 0), 2)
