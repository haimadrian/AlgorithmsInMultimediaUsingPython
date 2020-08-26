__author__ = "Haim Adrian"

import tkinter as tk
import tkinter.filedialog as tkfiledialog
import os
import view.controls as ctl
import numpy as np
from threading import Thread
from tkinter.ttk import Style
from tkinter import messagebox
from harris_detector import corners_and_line_intersection_detector
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MainDialog(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(background=ctl.BACKGROUND_COLOR)
        toplevel = self.winfo_toplevel()
        toplevel.title('Corners Detector')
        toplevel.iconbitmap(os.path.abspath(os.path.join('resource', 'corners-icon.ico')))

        # Declare all of the instance attributes here, and initialize them in separate methods for code separation
        # Keep them as attributes so we will not have issues with garbage collection. Especially with the PhotoImage
        self.__title_frame = None  # tk.Frame
        self.__action_frame = None  # tk.Frame
        self.__status_frame = None  # tk.Frame
        self.__figure_frame = None  # tk.Frame
        self.__title = None  # tk.Label
        self.__status_bar = None  # tk.Label
        self.__progress_bar = None  # tk.Progressbar
        self.__go_button = None  # tk.Button
        self.__open_file_button = None  # tk.Button
        self.__canny_check_var = None  # tk.IntVar  - to hold the value of the checkbox
        self.__canny_checkbutton = None  # tk.Checkbutton
        self.__file_path_entry = None  # tk.Entry
        self.__magnifying_icon = None  # tk.PhotoImage
        self.__figure = None  # A reference to pyplot figure, so we can destroy it when there is a new input
        self.__style = None  # tk.ttk.Style
        self.__running = False  # Indication of when we wait for the Harris Detector worker to finish
        self.__image = None  # A reference to the input image. It is being set by the Harris Detector action
        self.__processed_image = None  # A reference to the processed image (outcome). It is being set by the Harris Detector action
        self.__error = False  # Indication for a failure during Harris Detector algorithm

        self.__style = Style(master)
        self.__style.configure('TButton', font=('Calibri', 14, 'bold'), borderwidth='1', foreground='green', background='#3592C4')
        self.__style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'green')])

        self.create_title_section(master)
        self.create_action_section(master)
        self.create_status_section(master)
        self.create_workarea_section(master)

        master.bind('<Return>', self.on_enter_pressed)
        master.geometry("800x600")

    def create_title_section(self, master):
        """
        Title area contains a frame with a label in it.
        :param master: Master dialog to add the frame to
        :return: None
        """
        self.__title_frame = ctl.create_frame(master, tk.X)
        self.__title = tk.Label(master=self.__title_frame, text='Corners Detector', font=('Calibri', 22, 'bold'),
                                background=ctl.BACKGROUND_COLOR, foreground=ctl.FOREGROUND_COLOR)
        self.__title.pack(fill=tk.X)

    def create_action_section(self, master):
        """
        Action area contains a frame with an entry (text edit for image path), open file dialog button and Go button.
        Open file dialog button will display an open file dialog to select image
        Go button will execute Harris Detector action on the selected image
        :param master: Master dialog to add the frame to
        :return: None
        """
        self.__action_frame = ctl.create_frame(master, tk.X)
        self.__magnifying_icon = tk.PhotoImage(file=os.path.abspath(os.path.join('resource', 'magnifying-icon.png')))
        ctl.create_pad(self.__action_frame, tk.LEFT)
        self.__file_path_entry = tk.Entry(master=self.__action_frame,
                                          background=ctl.BACKGROUND_EDITOR_COLOR, foreground=ctl.FOREGROUND_EDITOR_COLOR)
        self.__file_path_entry.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.__open_file_button = tk.ttk.Button(master=self.__action_frame, image=self.__magnifying_icon,
                                                command=self.open_file_action, style='TButton', width=4)
        self.__open_file_button.pack(side=tk.LEFT)
        ctl.create_pad(self.__action_frame, tk.LEFT)

        self.__go_button = tk.ttk.Button(master=self.__action_frame, text='Go!', command=self.on_enter_pressed, style='TButton', width=5)
        ctl.create_pad(self.__action_frame, tk.RIGHT)
        self.__go_button.pack(side=tk.RIGHT)

        # Get a second line in the actions area, so the checkbox will be under the entry
        helper_frame = ctl.create_frame(master, tk.X)
        self.__canny_check_var = tk.IntVar()
        self.__canny_checkbutton = tk.Checkbutton(helper_frame, text='Go through Canny Edge Detection', padx=5, pady=5,
                                                  background=ctl.BACKGROUND_COLOR, foreground=ctl.FOREGROUND_EDITOR_COLOR,
                                                  activebackground=ctl.BACKGROUND_COLOR, activeforeground=ctl.FOREGROUND_EDITOR_COLOR,
                                                  font=('Calibri', 12), selectcolor=ctl.BACKGROUND_EDITOR_COLOR,
                                                  variable=self.__canny_check_var)
        self.__canny_checkbutton.pack(side=tk.LEFT)

    def create_status_section(self, master):
        """
        Status area contains a progress bar which we put at the bottom of the frame, to show a progress indication when
        the algorithm is executing. (Can take some seconds)
        We also add a label into the progress bar to use it as a status bar as well
        :param master: Master dialog to add the frame to
        :return: None
        """
        self.__status_frame = ctl.create_frame(master, tk.X)
        self.__status_frame.pack(fill=tk.X, side=tk.BOTTOM, anchor=tk.S)
        # Add label into the layout
        self.__style.layout('text.Horizontal.TProgressbar',
                            [('Horizontal.Progressbar.trough',
                              {'children': [('Horizontal.Progressbar.pbar', {'side': 'left', 'sticky': 's'})], 'sticky': 'swe'}),
                             ('Horizontal.Progressbar.label', {'sticky': 'we'})])
        self.__progress_bar = tk.ttk.Progressbar(master=self.__status_frame, orient=tk.HORIZONTAL, style='text.Horizontal.TProgressbar',
                                                 length=1, mode='determinate', value=0, maximum=75)
        self.__progress_bar.pack(fill=tk.X)
        self.update_status('Open an image and click the Go button')

    def create_workarea_section(self, master):
        """
        Workarea contains a frame onto which we are displaying the plots when we finish executing Harris Detector algorithm
        :param master: Master dialog to add the frame to
        :return: None
        """
        ctl.create_pad(master, tk.LEFT)
        ctl.create_pad(master, tk.RIGHT)
        ctl.create_pad(master, tk.BOTTOM)
        self.__figure_frame = ctl.create_frame(master, tk.BOTH)
        self.__figure_frame.configure(background='white')  # Make it white because I could not modify the PyPlot background

    def update_status(self, text):
        """
        Updates the text of the progress bar (status bar) with the specified text
        :param text: The text to set into the status bar
        :return: None
        """
        self.__style.configure('text.Horizontal.TProgressbar', text=text)

    def start_progress(self):
        """
        Start an indeterminate progress in the progress bar, for visualizing process.
        We also start checking the job queue to detect if the algorithm has finished its execution so we can display the outcome
        :return: None
        """
        self.set_user_components_state('disabled')
        self.__image = self.__processed_image = None
        self.__progress_bar.configure(mode='indeterminate')
        self.__progress_bar.start()
        self.__running = True
        self.periodically_check_outcome()

        if self.__figure is not None:
            self.__figure.set_visible(False)
            self.__figure.clear()
            self.__figure = None

            # Remove all children so we will not have issues with pyplot's painting
            for child in self.__figure_frame.winfo_children():
                child.destroy()

    def stop_progress(self):
        """
        Stops the progress of the progress bar, and the periodic check of the job queue
        :return: None
        """
        self.__progress_bar.stop()
        self.__progress_bar.configure(mode='determinate')
        self.__progress_bar['value'] = 0
        self.__running = False
        self.set_user_components_state('normal')

    def set_user_components_state(self, new_state):
        """
        Sets the state of user components to 'normal' or 'disabled'.
        When the algorithm is running in background, we disable the user components so there won't be a mess
        :param new_state: The new state to set. Can be one of 'normal' or 'disabled'
        :return: None
        """
        self.__go_button['state'] = new_state
        self.__open_file_button['state'] = new_state
        self.__file_path_entry['state'] = new_state

    def open_file_action(self):
        """
        Displaying a file open dialog in image selecting mode, to select an image for executing the algorithm on
        :return: None
        """
        file_name = tkfiledialog.askopenfilename(filetypes=[("Image File", '.jpg')])
        self.__file_path_entry.delete(0, 'end')
        self.__file_path_entry.insert(0, file_name)

    def on_enter_pressed(self, event=None):
        """
        This event is raised whenever user presses the Go button or Enter
        In this case we are going to execute Harris Detector algorithm using the selected image, in case there is a valid selection.
        :param event: The keypress event (We register on the master frame)
        :return: None
        """
        file_path = self.__file_path_entry.get().strip()
        if file_path == '':
            messagebox.showerror('Illegal Input', 'Please select an image first')
            return None

        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            messagebox.showerror('Illegal Input', 'Selected image is not a file or it does not exist:\n{}'.format(file_path))
            return None

        if not self.__running:
            self.start_progress()

            # Run it in background so the progress bar will not get blocked. (We cannot block te gui thread)
            t = Thread(target=self.execute_harris_detector, args=(file_path,))
            t.start()
        else:
            print('Already running. Cannot run multiple detections in parallel.')

    def execute_harris_detector(self, path):
        """
        The job of executing Harris Detector algorithm.
        It takes time so we have a specific action for that, such that we can run it using a background thread
        :param path: Path to the selected image
        :return: None
        """
        self.__image, self.__processed_image = corners_and_line_intersection_detector(path,
                                                                                      lambda text: self.update_status(text),
                                                                                      bool(self.__canny_check_var.get()))
        if self.__image is None or self.__processed_image is None:
            self.__error = True

    def show_images(self, img, processed_image):
        """
        When Harris Detector job has finished we display the results as embedded figure
        :param img: Original image
        :param processed_image: Image with corner marks
        :return: None
        """
        self.__figure = Figure(figsize=(5, 5), dpi=100)
        axes = self.__figure.add_subplot(121)
        axes.imshow(np.uint8(img[:, :, ::-1]))
        axes = self.__figure.add_subplot(122)
        axes.imshow(np.uint8(processed_image[:, :, ::-1]))
        self.__figure.subplots_adjust(0.05, 0.2, 0.95, 0.9, 0.2, 0.2)
        # figure.tight_layout(pad=1.0)
        canvas = FigureCanvasTkAgg(self.__figure, self.__figure_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.__figure_frame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def periodically_check_outcome(self):
        """
        Check every 200 ms if there is something new to show, which means a harris_detector worker has finished
        and we can pick the output and show it in the GUI
        """
        if self.__error:
            self.__error = False
            self.stop_progress()
            messagebox.showerror('Error', 'Error has occurred while trying to detect corners')
            self.__image = self.__processed_image = None
            return None

        if self.__image is not None and self.__processed_image is not None:
            self.stop_progress()
            # Plot the images, embedded within our dialog rather than popping up another dialog.
            self.show_images(self.__image, self.__processed_image)

        if self.__running:
            self.master.after(200, self.periodically_check_outcome)
