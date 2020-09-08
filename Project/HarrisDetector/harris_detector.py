__author__ = "Haim Adrian"

from timeit import default_timer as timer
from harris_detector_logic import *
from util.settings import Settings


def corners_and_line_intersection_detector(image_path, console_consumer=None, progress_consumer=None, is_using_canny=False,
                                           is_applying_gauss=False, settings=Settings()):
    """
    Main entry point to the Harris Detector algorithm
    We call this method from main frame in order to open an image, detect corners in it, and return both the image and
    a copy of the image with the corners marked out
    :param image_path: Path of the image to read
    :param console_consumer: A lambda / function to handle status updates
    :param progress_consumer: A lambda / function to handle progress updates
    :param is_using_canny: Whether we should detect edges using Canny Edge Detection before Harris Detector, or not
    :param is_applying_gauss: Whether to apply Gaussian Blur before executing Harris Corner Detector
    :param settings: Settings to know how to execute the algorithm
    :return: image, image_with_marks
    """
    start = timer()
    img = cv2.imread(image_path)
    progress = do_progress(progress_consumer, 0, 1)

    success = False

    if img is None:
        log(console_consumer, 'Unable to open image:', image_path)
        image = None
    else:
        image = img.copy()
        if is_applying_gauss:
            log(console_consumer, 'Applying Gaussian Blur...')
            image = apply_gaussian_blur(image)  # yields either 3D or 2D, depends on the image
            progress = do_progress(progress_consumer, progress, 4)

        if is_using_canny:
            log(console_consumer, 'Running Canny Edge Detection...')
            image = cv2.Canny(image, settings.canny_min_thresh, settings.canny_max_thresh)  # yields 2D
            progress = do_progress(progress_consumer, progress, 5)

        log(console_consumer, 'Detecting corners...')
        max_progress = 60
        harris_scores = find_harris_corners(image, settings.harris_free_parameter, settings.neighborhood_size, console_consumer,
                                            progress_consumer, progress, max_progress)
        progress = max_progress

        if harris_scores is None:
            log(console_consumer, 'Error has occurred while detecting corners. Result was None')
            image = None
        else:
            success = True
            image = img.copy()
            if image.ndim == 2:
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            # Mark the corners
            log(console_consumer, 'Marking detected interest points...')
            helper_image = enhance_corners_accuracy(harris_scores, image, settings)
            mark_corners(image, helper_image, settings, progress_consumer, progress)

    time_took = timer() - start
    do_progress(progress_consumer, 0, 100)
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


def mark_corners(image, harris_scores, settings, progress_consumer, progress):
    """
    A helper method we use to make the marks of corner as rectangles or bold circles, rather than single pixels.
    Use a blank image (black), then light up the pixels that have been found by Harris Detector
    This way we create a clear image, without any noise, and then we can safely dilate the image to make the
    lights thicker, find the contours and then paint rectangles using the contours
    :param image: The image to paint the marks on
    :param harris_scores: The R values (scores) from Harris Detector algorithm
    :param settings: Settings for getting dilate size and color
    :param progress_consumer: A lambda / function to handle progress updates
    :param progress: Starting value of the progress, to show progress relative to this value
    :return: None
    """
    corners_color = settings.corners_color[::-1]
    progress_steps_left = 100 - progress
    progress_step = progress_steps_left / harris_scores.shape[0]
    for i in range(harris_scores.shape[0]):
        for j in range(harris_scores.shape[1]):
            if harris_scores[i, j] == 255:
                top = i - settings.dilate_size
                left = j - settings.dilate_size
                bottom = i + settings.dilate_size
                right = j + settings.dilate_size

                if settings.is_using_rect_mark:
                    # Draw a green rectangle to visualize the bounding rect
                    cv2.rectangle(image, (left, top), (right, bottom), corners_color, 2)
                else:
                    cv2.circle(image, (j, i), 2, settings.corners_color[::-1], 2)
        progress = do_progress(progress_consumer, progress, progress_step)
    return None


def enhance_corners_accuracy(harris_scores, image, settings):
    """
    This method created for enhancing the corners detection by using the detected corners with cv2.cornerSubPix in order
    to find the exact center of a corner, thus making it more accurate.
    After using this method we make the pixels found by this method bolded by using a circle (dot) or rectangle
    :param harris_scores: Harris scores, to make them more accurate
    :param image: The original image is needed for cv2.cornerSubPix in order to check where exactly the center of a corner is
    :param settings: Setting for fetching harris score threshold from
    :return: Centers of each corner in an image with same shape of original image
    """
    helper_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    dst = cv2.dilate(harris_scores, None)
    ret, dst = cv2.threshold(dst, settings.harris_score_threshold * dst.max(), 255, 0)
    dst = np.uint8(dst)

    # Find centroids
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    if image.ndim == 3:
        twoD = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        twoD = image

    # Define the criteria to stop and refine the corners
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, settings.harris_score_threshold)
    corners = cv2.cornerSubPix(twoD, np.float32(centroids), (5, 5), (-1, -1), criteria)

    # Now draw them
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    helper_image[res[:, 3], res[:, 2]] = 255

    # For some reason we get the center of the image marked even though there is nothing there.
    # So here I unmark it, taking the risk of missing a corner.
    i = int(helper_image.shape[0] / 2)
    j = int(helper_image.shape[1] / 2)
    helper_image[i - 4: i + 5, j - 4: j + 5] = 0

    return helper_image
