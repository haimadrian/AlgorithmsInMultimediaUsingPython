__author__ = "Haim Adrian"

import matplotlib
matplotlib.use('TkAgg')  # So we can embed plots in our dialog
import tkinter as tk
import view.maindialog as maindialog
import view.controls as ctl


if __name__ == '__main__':
    window = tk.Tk()

    maindialog.MainDialog(window)
    ctl.center(window)

    # Run the event loop
    window.mainloop()
