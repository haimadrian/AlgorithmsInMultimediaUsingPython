__author__ = "Haim Adrian"

import tkinter as tk


BACKGROUND_COLOR = '#3C3F41'
FOREGROUND_COLOR = '#A9A9A9'
BACKGROUND_EDITOR_COLOR = '#2B2B2B'
FOREGROUND_EDITOR_COLOR = '#FFFFFF'


def create_pad(master, side):
    """
    We use this as a padding inside a frame. We create an empty label to force a pad between components
    This is some weird hack, but the grid() does not snap to the frame when resizing it, so we use frames.
    :param master: Owner of the label
    :param side: Where the label should be aligned to. (e.g. LEFT or RIGHT)
    :return: None
    """
    tk.Label(master=master, text=' ', background=BACKGROUND_COLOR).pack(side=side)


def create_frame(master, fill):
    """
    A utility method used for creating frame under a specified master using specified fill, with dark background
    :param master: Owner of the created frame
    :param fill: How the frame should fill its container. e.g. X, Y, BOTH
    :return: The created frame
    """
    frame = tk.Frame(master=master, background=BACKGROUND_COLOR)
    frame.pack(fill=fill)
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
                                 font=('Calibri', 12), selectcolor=BACKGROUND_EDITOR_COLOR, variable=check_var)
    checkbutton.pack(side=side)
    return checkbutton, check_var


def create_spinbox(master, values, side, width):
    """
    A utility method used for creating spinbox under a specified master at specified side, with dark background
    :param master: Owner of the created checkbutton
    :param values: A tuple containing valid values for this widget
    :param side: Where the spinbox should be
    :param width: The width of the spinbox
    :return: The created check button, followed by its IntVar
    """
    spinbox = tk.Spinbox(master=master, width=width, values=values, font=('Calibri', 12),
                         selectbackground=BACKGROUND_EDITOR_COLOR, selectforeground=FOREGROUND_EDITOR_COLOR,
                         background=BACKGROUND_EDITOR_COLOR, foreground=FOREGROUND_EDITOR_COLOR)
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
