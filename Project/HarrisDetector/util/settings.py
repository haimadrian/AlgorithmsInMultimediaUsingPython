__author__ = "Haim Adrian"

import os
from ast import literal_eval

SETTINGS_FILE_NAME = 'settings.txt'


class Settings:
    """
    Settings class is used to let user to configure some advanced properties, for the application and for the Harris
    Detector algorithm itself.
    This class is written to file so we can save settings between launches of the application.
    """

    def __init__(self, harris_score_threshold=0.01, harris_free_parameter=0.04, neighborhood_size=5, corners_color=(0, 255, 0),
                 canny_min_thresh=100, canny_max_thresh=200, is_using_rect_mark=True, dilate_size=20):
        """
        Constructs a new Settings instance.
        :param harris_score_threshold: See :py:attr:`~.settings.Settings.harris_score_threshold`
        :param harris_free_parameter: See :py:attr:`~settings.Settings.harris_free_parameter`
        :param neighborhood_size: See :py:attr:`~settings.Settings.neighborhood_size`
        :param corners_color: See :py:attr:`~settings.Settings.corners_color`
        :param canny_min_thresh: See :py:attr:`~settings.Settings.canny_min_thresh`
        :param canny_max_thresh: See :py:attr:`~settings.Settings.canny_max_thresh`
        :param is_using_rect_mark: See :py:attr:`~settings.Settings.is_using_rect_mark`
        :param dilate_size: See :py:attr:`~settings.Settings.dilate_size`
        """
        self.harris_score_threshold = harris_score_threshold
        self.harris_free_parameter = harris_free_parameter
        self.neighborhood_size = neighborhood_size
        self.corners_color = corners_color
        self.canny_min_thresh = canny_min_thresh
        self.canny_max_thresh = canny_max_thresh
        self.is_using_rect_mark = is_using_rect_mark
        self.dilate_size = dilate_size

    @property
    def harris_score_threshold(self):
        """
        The threshold we use in order to detect Harris corners.
        By default the value is set to 0.01, but it can be modified based on input images.
        We use this threshold as percentage. All scores above threshold*max_score will be considered as corners.
        :return: The threshold to use for collecting corners
        """
        return self.__harris_score_threshold

    @harris_score_threshold.setter
    def harris_score_threshold(self, value):
        self.__harris_score_threshold = value

    @property
    def harris_free_parameter(self):
        """
        Harris free parameter is the 'k' variable from the equation which gives ranking to pixels.
        Default value is 0.04
        :return: Harris free parameter value
        """
        return self.__harris_free_parameter

    @harris_free_parameter.setter
    def harris_free_parameter(self, value):
        self.__harris_free_parameter = value

    @property
    def neighborhood_size(self):
        """
        This is the window size we use in order to rank pixels in image while using Harris Detector for detecting corners.
        Default value is 5
        :return: Window size for Harris Detector
        """
        return self.__neighborhood_size

    @neighborhood_size.setter
    def neighborhood_size(self, value):
        self.__neighborhood_size = value

    @property
    def corners_color(self):
        """
        The color (RGB Tuple) we use for drawing rectangles/dots as a mark sign for corners.
        Default value is (0, 255, 0) - Green
        :return: Marks color
        """
        return self.__corners_color

    @corners_color.setter
    def corners_color(self, value):
        self.__corners_color = value

    @property
    def canny_min_thresh(self):
        """
        Minimum threshold to use for Canny Edge Detection algorithm.
        Default value is 100
        :return: Minimum threshold for Canny Edge
        """
        return self.__canny_min_thresh

    @canny_min_thresh.setter
    def canny_min_thresh(self, value):
        self.__canny_min_thresh = value

    @property
    def canny_max_thresh(self):
        """
        Maximum threshold to use for Canny Edge Detection algorithm.
        Default value is 200
        :return: Maximum threshold for Canny Edge
        """
        return self.__canny_max_thresh

    @canny_max_thresh.setter
    def canny_max_thresh(self, value):
        self.__canny_max_thresh = value

    @property
    def is_using_rect_mark(self):
        """
        :return: Whether we use rectangles as corners marking, or dots
        """
        return self.__is_using_rect_mark

    @is_using_rect_mark.setter
    def is_using_rect_mark(self, value):
        self.__is_using_rect_mark = value

    @property
    def dilate_size(self):
        """
        We dilate Harry Scores in order to make the dots thicker or rectangles wider such that it will be easy to
        understand where the corners are. We use it when drawing the marks.
        Default value is 20
        :return: The size to use as kernel for cv2.dilate (Affect rectangle size)
        """
        return self.__dilate_size

    @dilate_size.setter
    def dilate_size(self, value):
        self.__dilate_size = value

    def save(self):
        """
        Store settings to file
        :return: self
        """
        print('Storing settings to file:', SETTINGS_FILE_NAME)
        with open(SETTINGS_FILE_NAME, 'w') as out_file:
            out_file.writelines([str(self.harris_score_threshold) + '\n',
                                 str(self.harris_free_parameter) + '\n',
                                 str(self.neighborhood_size) + '\n',
                                 str(self.corners_color) + '\n',
                                 str(self.canny_min_thresh) + '\n',
                                 str(self.canny_max_thresh) + '\n',
                                 str(self.dilate_size) + '\n',
                                 str(self.is_using_rect_mark) + '\n'])
        return self

    def load(self):
        """
        Load settings from a previously saved file.
        Does nothing if the file does not exist
        :return: self
        """
        if os.path.exists(SETTINGS_FILE_NAME) and os.path.isfile(SETTINGS_FILE_NAME):
            try:
                print('Loading settings from file:', SETTINGS_FILE_NAME)
                with open(SETTINGS_FILE_NAME, 'r') as in_file:
                    self.harris_score_threshold = float(in_file.readline().strip())
                    self.harris_free_parameter = float(in_file.readline().strip())
                    self.neighborhood_size = int(in_file.readline().strip())
                    self.corners_color = literal_eval(in_file.readline().strip())
                    self.canny_min_thresh = float(in_file.readline().strip())
                    self.canny_max_thresh = float(in_file.readline().strip())
                    self.dilate_size = int(in_file.readline().strip())
                    self.is_using_rect_mark = (in_file.readline().strip() == 'True')

                    if not 0 < self.dilate_size <= 100:
                        self.dilate_size = 20
            except Exception as e:
                print('Error has occurred while reading settings file. File has to be overridden')
                print(e)
        return self
