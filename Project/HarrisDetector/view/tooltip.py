__author__ = "StackOverflow"

import tkinter as tk
import view.controls as ctl


class Tooltip(object):
    """
    Create a tooltip for a given widget
    Credits: https://stackoverflow.com/a/36221216/8124906
    """
    def __init__(self, widget, text='widget info'):
        self.wait_time = 500  # milliseconds
        self.wrap_length = 400  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.showtip)

    def unschedule(self):
        iid = self.id
        self.id = None
        if iid:
            self.widget.after_cancel(iid)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 40
        self.tw = tk.Toplevel(self.widget)

        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left', relief='solid', borderwidth=1,
                         background=ctl.BACKGROUND_TOOLTIP_COLOR, foreground=ctl.FOREGROUND_TOOLTIP_COLOR,
                         wraplength=self.wrap_length, font=ctl.FONT_REGULAR)
        label.pack(ipadx=5, ipady=5)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
