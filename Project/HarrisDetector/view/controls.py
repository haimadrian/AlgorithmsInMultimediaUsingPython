__author__ = "Haim Adrian"

import tkinter as tk


BACKGROUND_COLOR = '#3C3F41'
FOREGROUND_COLOR = '#A9A9A9'
BACKGROUND_EDITOR_COLOR = '#2B2B2B'
FOREGROUND_EDITOR_COLOR = '#FFFFFF'
BACKGROUND_TOOLTIP_COLOR = '#4B4D4D'
FOREGROUND_TOOLTIP_COLOR = '#A9A9A9'
ACCEPT_COLOR = '#3592C4'
FONT_REGULAR = ('Calibri', 12)
FONT_REGULAR_BOLD = ('Calibri', 12, 'bold')
FONT_BUTTON = ('Calibri', 14, 'bold')
FONT_TITLE = ('Calibri', 22, 'bold')


def create_pad(master, side):
    """
    We use this as a padding inside a frame. We create an empty label to force a pad between components
    This is some weird hack, but the grid() does not snap to the frame when resizing it, so we use frames.
    :param master: Owner of the label
    :param side: Where the label should be aligned to. (e.g. LEFT or RIGHT)
    :return: None
    """
    tk.Label(master=master, text=' ', background=BACKGROUND_COLOR).pack(side=side)


def create_label(master, text):
    """
    Create a label with dark background and regular font
    :param master: Owner of the label
    :param text: The text to set to the label
    :return: The label
    """
    return tk.Label(master, text=text, background=BACKGROUND_COLOR, foreground=FOREGROUND_EDITOR_COLOR, font=FONT_REGULAR)


def create_title(master, text):
    """
    Create a label with dark background and title font
    :param master: Owner of the label
    :param text: The text to set to the label
    :return: The label
    """
    return tk.Label(master, text=text, background=BACKGROUND_COLOR, foreground=FOREGROUND_EDITOR_COLOR, font=FONT_TITLE)


def create_entry(master, validate_command=None):
    """
    Create an editor (text field) with dark background
    :param master: Owner of the label
    :param validate_command: Optional validation command
    :return: The entry
    """
    if validate_command:
        return tk.Entry(master=master, background=BACKGROUND_EDITOR_COLOR, foreground=FOREGROUND_EDITOR_COLOR,
                        validate='all', validatecommand=validate_command)
    return tk.Entry(master=master, background=BACKGROUND_EDITOR_COLOR, foreground=FOREGROUND_EDITOR_COLOR)


def create_frame(master, fill, padx=5, pady=5):
    """
    A utility method used for creating frame under a specified master using specified fill, with dark background
    :param master: Owner of the created frame
    :param fill: How the frame should fill its container. e.g. X, Y, BOTH
    :param padx: Horizontal padding
    :param pady: Vertical padding
    :return: The created frame
    """
    frame = tk.Frame(master=master, background=BACKGROUND_COLOR)
    frame.pack(fill=fill, padx=padx, pady=pady)
    return frame


def create_checkbutton(master, text, side):
    """
    A utility method used for creating checkbutton under a specified master at specified side, with dark background
    :param master: Owner of the created checkbutton
    :param text: The text to set to the checkbutton
    :param side: Where the checkbutton should be
    :return: The created check button, followed by its IntVar
    """
    check_var = tk.IntVar()
    checkbutton = tk.Checkbutton(master, text=text, padx=5, pady=5,
                                 background=BACKGROUND_COLOR, foreground=FOREGROUND_EDITOR_COLOR,
                                 activebackground=BACKGROUND_COLOR, activeforeground=FOREGROUND_EDITOR_COLOR,
                                 font=FONT_REGULAR, selectcolor=BACKGROUND_EDITOR_COLOR, variable=check_var)
    checkbutton.pack(side=side)
    return checkbutton, check_var


def create_spinbox(master, values, width, validate_command, side=None):
    """
    A utility method used for creating spinbox under a specified master at specified side, with dark background
    :param master: Owner of the created checkbutton
    :param values: A tuple containing valid values for this widget
    :param side: Where the spinbox should be
    :param width: The width of the spinbox
    :param validate_command Validator function to validate the input of the spinbox (func that receives a string and returns boolean)
    :return: The created check button, followed by its IntVar
    """
    spinbox = tk.Spinbox(master=master, width=width, values=values, font=FONT_REGULAR, validate='all', validatecommand=validate_command,
                         background=BACKGROUND_EDITOR_COLOR, foreground=FOREGROUND_EDITOR_COLOR)
    if side:
        spinbox.pack(side=side)
    return spinbox


def center(window):
    """
    Centers a tkinter window within the screen
    :param window: The window to center
    """
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()


def color_to_hex(color):
    if not isinstance(color, tuple) or len(color) != 3:
        print('color_to_hex: Specified color was not a tuple or its dimension does not fit to RGB. Was:', color)
        return '#00FF00'

    def clamp(x):
        return max(0, min(x, 255))

    return '#{0:02x}{1:02x}{2:02x}'.format(clamp(color[0]), clamp(color[1]), clamp(color[2]))
