__author__ = "Haim Adrian"

import numpy as np
import tkinter as tk
import os
import view.controls as ctl
from util.settings import Settings
from tkinter import messagebox
from ast import literal_eval


def reset_text(widget, value):
    widget.delete(0, tk.END)
    widget.insert(0, str(value))


def is_numeric(x):
    import re

    # Store a compiled regex onto the function so we will not have to recompile it over and over
    if not hasattr(is_numeric, 'numericRegex'):
        # Do not accept negative values (define + in the regex only, without -)
        is_numeric.numericRegex = re.compile(r"^([+]?\d*)\.?\d*$")
    return len(str(x).strip()) > 0 and is_numeric.numericRegex.match(str(x).strip()) is not None


def is_tuple(x):
    import re

    # Store a compiled regex onto the function so we will not have to recompile it over and over
    if not hasattr(is_tuple, 'tupleRegex'):
        is_tuple.tupleRegex = re.compile(r"^ *\( *\d+ *, *\d+ *, *\d+ *\) *$")
    return len(str(x).strip()) > 0 and is_tuple.tupleRegex.match(str(x).strip()) is not None


def numeric_validator(widget, old_text, new_text):
    """
    A function used to validate the input of an entry, to make sure it is numeric
    :param widget: Sender widget
    :param old_text: Input text before the change
    :param new_text: Input text
    :return: Whether text is a valid number or not
    """
    is_valid = is_numeric(new_text) or new_text == ''

    if not is_valid:
        messagebox.showerror('Illegal Input', 'Input must be numeric. Was: {}'.format(new_text))
        widget.delete(0, tk.END)
        widget.insert(0, old_text)
        widget.focus_set()

    return is_valid


class SettingsDialog(tk.Toplevel):
    def __init__(self, parent, settings: Settings):
        tk.Toplevel.__init__(self, parent)

        # Hide the dialog in the task bar. Let it be an inner window of the parent window
        self.transient(parent)

        self.title('Settings')
        self.iconbitmap(os.path.abspath(os.path.join('resource', 'settings-icon.ico')))
        self.config(background=ctl.BACKGROUND_COLOR)
        self.parent = parent

        # The result of the dialog: settings.Settings object
        self.__result = None
        self.closing = False  # A marker to see if we are cancelling the window, to avoid of validating input
        self.settings = settings
        self.rect_mark_check_var = None  # tk.IntVar  - to hold the value of the rect_mark checkbox
        self.rect_mark_checkbutton = None  # tk.Checkbutton
        self.mark_color = settings.corners_color  # Tuple (R, G, B)
        self.mark_color_entry = None  # tk.Button
        self.dilate_size_spinbox = None  # tk.Spinbox
        self.harris_score_threshold_spinbox = None  # tk.Entry
        self.harris_free_parameter_spinbox = None  # tk.Entry
        self.neighborhood_size_spinbox = None  # tk.Entry
        self.canny_min_threshold_entry = None  # tk.Entry
        self.canny_max_threshold_entry = None  # tk.Entry

        # Build the body
        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        # Dialog buttons
        self.buttonbox()

        # Make the dialog modal
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        # Make sure an explicit close is treated as a CANCEL
        self.protocol("WM_DELETE_WINDOW", self.cancel)

        ctl.center(self)
        self.initial_focus.focus_set()
        self.wait_window(self)

    @property
    def result(self):
        """
        The result of settings dialog is None in case user cancelled the dialog, or util.settings.Settings object
        if user approved the dialog
        :return: The settings
        """
        return self.__result

    def body(self, master):
        """
        Dialog body - a frame containing all setting controls
        :param master: Master window
        :return: The created frame
        """
        master.columnconfigure(0, weight=1)
        frame = tk.Frame(master, bg=ctl.BACKGROUND_COLOR)
        frame.grid(row=0, column=0, columnspan=2, sticky=tk.EW)
        frame.columnconfigure(1, weight=1)
        self.rect_mark_checkbutton, self.rect_mark_check_var = ctl.create_checkbutton(frame, 'Use rectangle mark (or dots)', tk.LEFT)
        self.rect_mark_checkbutton.grid(row=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
        self.mark_color_entry = tk.Entry(frame, font=ctl.FONT_REGULAR_BOLD,
                                         foreground='white', background=ctl.color_to_hex(self.settings.corners_color))
        self.mark_color_entry.bind('<FocusOut>',
                                   lambda event: self.color_validator_cmd(self.mark_color_entry.get()))
        self.mark_color_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        ctl.create_label(frame, text='Bounding rectangle size').grid(row=1, padx=5, pady=5, sticky=tk.W)
        # Registering validation command
        self.dilate_size_spinbox = ctl.create_spinbox(frame, (1, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50), 5,
                                                      (self.master.register(self.dilate_size_validator), '%s', '%P'))
        self.dilate_size_spinbox.bind('<FocusOut>',
                                      lambda event: self.dilate_size_validator(self.settings.dilate_size, self.dilate_size_spinbox.get()))
        self.dilate_size_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        ctl.create_label(frame, text='Harris score threshold').grid(row=2, padx=5, pady=5, sticky=tk.W)
        # %W is the widget, %s is the text before edit, %P is the text after edit
        self.harris_score_threshold_spinbox = ctl.create_spinbox(frame, tuple(np.arange(0.01, 1, 0.01)), 5,
                                                                 (self.master.register(self.numeric_validator_cmd), '%W', '%s', '%P'))
        self.harris_score_threshold_spinbox.bind('<FocusOut>',
                                                 lambda event: numeric_validator(self.harris_score_threshold_spinbox,
                                                                                 self.settings.harris_score_threshold,
                                                                                 self.harris_score_threshold_spinbox.get()) if not self.closing else None)
        self.harris_score_threshold_spinbox.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        ctl.create_label(frame, text='Harris free parameter (k)').grid(row=3, padx=5, pady=5, sticky=tk.W)
        self.harris_free_parameter_spinbox = ctl.create_spinbox(frame, (0.04, 0.05, 0.06), 5,
                                                                (self.master.register(self.numeric_validator_cmd), '%W', '%s', '%P'))
        self.harris_free_parameter_spinbox.bind('<FocusOut>',
                                                lambda event: numeric_validator(self.harris_free_parameter_spinbox,
                                                                                self.settings.harris_free_parameter,
                                                                                self.harris_free_parameter_spinbox.get()) if not self.closing else None)
        self.harris_free_parameter_spinbox.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        ctl.create_label(frame, text='Neighborhood size (Harris Matrix)').grid(row=4, padx=5, pady=5, sticky=tk.W)
        self.neighborhood_size_spinbox = ctl.create_spinbox(frame, tuple(range(3, 17, 2)), 5,
                                                            (self.master.register(self.numeric_validator_cmd), '%W', '%s', '%P'))
        self.neighborhood_size_spinbox.bind('<FocusOut>',
                                            lambda event: numeric_validator(self.neighborhood_size_spinbox,
                                                                            self.settings.neighborhood_size,
                                                                            self.neighborhood_size_spinbox.get()) if not self.closing else None)
        self.neighborhood_size_spinbox.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)

        ctl.create_label(frame, text='Canny Edge Min threshold').grid(row=5, padx=5, pady=5, sticky=tk.W)
        self.canny_min_threshold_entry = ctl.create_entry(frame, (self.master.register(self.numeric_validator_cmd), '%W', '%s', '%P'))
        self.canny_min_threshold_entry.bind('<FocusOut>',
                                            lambda event: numeric_validator(self.canny_min_threshold_entry,
                                                                            self.settings.canny_min_thresh,
                                                                            self.canny_min_threshold_entry.get()) if not self.closing else None)
        self.canny_min_threshold_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.EW)

        ctl.create_label(frame, text='Canny Edge Max threshold').grid(row=6, padx=5, pady=5, sticky=tk.W)
        self.canny_max_threshold_entry = ctl.create_entry(frame, (self.master.register(self.numeric_validator_cmd), '%W', '%s', '%P'))
        self.canny_max_threshold_entry.bind('<FocusOut>',
                                            lambda event: numeric_validator(self.canny_max_threshold_entry,
                                                                            self.settings.canny_max_thresh,
                                                                            self.canny_max_threshold_entry.get()) if not self.closing else None)
        self.canny_max_threshold_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.EW)

        # Load settings object to the editors
        self.init_settings()

        return frame

    def buttonbox(self):
        """
        OK and Cancel buttons
        :return: A frame containing the two buttons
        """
        box = ctl.create_frame(self, tk.BOTH, 0, 0)

        w = tk.Button(box, text="Reset", width=5, height=1, command=self.reset, font=ctl.FONT_REGULAR,
                      foreground='white', background=ctl.BACKGROUND_TOOLTIP_COLOR)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Cancel", width=10, command=self.cancel, font=ctl.FONT_BUTTON,
                      foreground='white', background='#C75450')
        w.pack(side=tk.RIGHT, padx=5, pady=5)
        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE, font=ctl.FONT_BUTTON,
                      foreground='white', background=ctl.ACCEPT_COLOR)
        w.pack(side=tk.RIGHT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

    def ok(self, event=None):
        """
        Command of the OK button
        :param event:
        :return: None
        """
        error_message = self.validate()
        if error_message is not None:
            messagebox.showerror('Illegal Input', error_message)

            # Put focus back
            self.initial_focus.focus_set()
            return

        # Validate the color specifically because we have not registered a validation command on it, but a
        # FocusOut binding only. The reason is we do want to allow several edits of the color as it is a Tuple string,
        # and validation command validates each single input char..
        if not self.color_validator_cmd(self.mark_color_entry.get()):
            self.initial_focus.focus_set()

        self.withdraw()
        self.update_idletasks()

        self.apply()
        self.cancel()

    def cancel(self, event=None):
        """
        Command of the CANCEL button
        :param event:
        :return: None
        """
        # Sign that we are closing the window, so we will not perform any validation during exit
        self.closing = True

        # Put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        """
        Validates the input
        :return: None if valid, error message otherwise
        """
        error = None

        harris_score = self.harris_score_threshold_spinbox.get()
        harris_param = self.harris_free_parameter_spinbox.get()
        neighborhood_size = self.neighborhood_size_spinbox.get()
        if not is_numeric(harris_score) or not 0 < float(harris_score) <= 1:
            error = 'Harris score threshold must be numeric in range (0, 1]'
        elif not is_numeric(harris_param) or not 0 < float(harris_param) <= 1:
            error = 'Harris free parameter must be numeric in range [0.04, 0.06]'
        elif not is_numeric(neighborhood_size) or not 3 <= float(neighborhood_size) <= 15 or int(float(neighborhood_size)) % 2 == 0:
            error = 'Neighborhood size must be an odd numeric in range [3, 15]'

        return error

    def apply(self):
        """
        Gather data into settings variable and set it as the result
        :return: None
        """
        self.__result = Settings(float(self.harris_score_threshold_spinbox.get()),
                                 float(self.harris_free_parameter_spinbox.get()),
                                 int(float(self.neighborhood_size_spinbox.get())),
                                 self.mark_color,
                                 int(float(self.canny_min_threshold_entry.get())),
                                 int(float(self.canny_max_threshold_entry.get())),
                                 bool(self.rect_mark_check_var.get()),
                                 int(float(self.dilate_size_spinbox.get())))

    def dilate_size_validator(self, old_text, new_text):
        """
        A function used to validate the input of dilate spinbox. (bounding rectangle size for marking corners)
        :param old_text: Text before change
        :param new_text: Input text (to the spinbox)
        :return: Whether text is a valid integer (in range) or not
        """
        if self.closing:
            return True

        is_valid = False
        if new_text.isdigit():
            if 0 < int(new_text) <= 100:
                is_valid = True
        elif new_text == '':
            is_valid = True

        if not is_valid:
            messagebox.showerror('Illegal Input', 'Dilate size (rectangle) must be between 1 to 100. Was: {}'.format(new_text))
            self.dilate_size_spinbox.delete(0, tk.END)
            self.dilate_size_spinbox.insert(0, old_text)
            self.dilate_size_spinbox.focus_set()

        return is_valid

    def numeric_validator_cmd(self, widget_name, old_text, new_text):
        """
        A function used to validate the input of an entry, to make sure it is numeric
        :param widget_name: Sender widget
        :param old_text: Input text before the change
        :param new_text: Input text
        :return: Whether text is a valid number or not
        """
        if self.closing:
            return True

        return numeric_validator(self.nametowidget(widget_name), old_text, new_text)

    def color_validator_cmd(self, text):
        if self.closing:
            return True

        is_valid = False
        text = text.strip()
        if is_tuple(text):
            is_valid = True
            for val in literal_eval(text):
                if val < 0 or val > 255:
                    is_valid = False
                    break
        elif text == '':
            is_valid = True

        if not is_valid:
            messagebox.showerror('Illegal Input', 'Input color is illegal. Was: {}'.format(text))
            self.mark_color_entry.focus_set()
        else:
            self.mark_color = literal_eval(text)
            self.mark_color_entry.configure(background=ctl.color_to_hex(self.mark_color))

        return is_valid

    def reset(self):
        """
        Resets settings to factory settings (defaults)
        :return: None
        """
        self.settings = Settings()
        self.init_settings()

    def init_settings(self):
        """
        Load settings from settings object into the editors
        :return: None
        """
        if self.settings.is_using_rect_mark:
            self.rect_mark_checkbutton.select()
        else:
            self.rect_mark_checkbutton.deselect()

        self.mark_color = self.settings.corners_color
        self.mark_color_entry.configure(background=ctl.color_to_hex(self.mark_color))
        reset_text(self.mark_color_entry, self.settings.corners_color)
        reset_text(self.dilate_size_spinbox, self.settings.dilate_size)
        reset_text(self.harris_score_threshold_spinbox, self.settings.harris_score_threshold)
        reset_text(self.harris_free_parameter_spinbox, self.settings.harris_free_parameter)
        reset_text(self.neighborhood_size_spinbox, self.settings.neighborhood_size)
        reset_text(self.canny_min_threshold_entry, int(self.settings.canny_min_thresh))
        reset_text(self.canny_max_threshold_entry, int(self.settings.canny_max_thresh))
