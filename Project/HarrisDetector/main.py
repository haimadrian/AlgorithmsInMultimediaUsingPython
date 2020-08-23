__author__ = "Haim Adrian"

import matplotlib
from harris_detector_logic import *

# Do it to see a new window when calling plt.show, and not within PyCharm.
matplotlib.use('TkAgg')


def corners_and_line_intersection_detector(image_path):
    img = cv2.imread(image_path)

    success = False

    if img is None:
        print('Unable to open image:', image_path)
    else:
        k = 0.04
        window_size = 5
        threshold = 10000.00

        print('Detecting corners...')
        corner_list, processed_image = find_harris_corners(img, k, window_size, threshold)

        if processed_image is None:
            print('Error has occurred while detecting corners. Result was None')
        else:
            success = True
            plt.figure('Corners and Line Intersection Detection')
            plot("Original Image", img, 121)
            plot("Processed Image", processed_image, 122)
            plt.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.1, 0.1)
            plt.show()

    print('Corners detection ended. Result:', 'Success' if success else 'Fail')


if __name__ == '__main__':
    corners_and_line_intersection_detector('squares.jpg')
    # corners_and_line_intersection_detector('rect_corner.jpg')
