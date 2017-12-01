import tkinter as Tk
from PIL import Image, ImageTk
from functools import partial
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import numpy as np
import pylab
import scipy

from web_scrape import *

class Window():
    def __init__(self, master):
        # create frame
        self.frame = Tk.Frame(master)

        # title and background color
        master.title('Wired.com Trends')
        master.configure(background='gray')

        # header Photo
        self.img = Image.open("./wired.jpg")
        # self.img = Image.open("D:\programming\PythonClassFiles\project\Super-Spice\wired.jpg")  # for my end
        self.img = self.img.resize((250, 50), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

        self.imgLabel = Tk.Label(image=self.photo)
        self.imgLabel.grid(row=0, columnspan=7)

        # buttons for each section of wired articles followed by placement
        self.business_button = Tk.Button(master, text="Business", height=3, width=10, command=partial(self.buttonAction, 1))
        self.business_button.grid(row=1, column=0, padx=5, pady=5)
        self.culture_button = Tk.Button(master, text="Culture", height=3, width=10, command=partial(self.buttonAction, 2))
        self.culture_button.grid(row=1, column=1, padx=5, pady=5)
        self.design_button = Tk.Button(master, text="Design", height=3, width=10, command=partial(self.buttonAction, 3))
        self.design_button.grid(row=1, column=2, padx=5, pady=5)
        self.gear_button = Tk.Button(master, text="Gear", height=3, width=10, command=partial(self.buttonAction, 4))
        self.gear_button.grid(row=1, column=3, padx=5, pady=5)
        self.science_button = Tk.Button(master, text="Science", height=3, width=10, command=partial(self.buttonAction, 5))
        self.science_button.grid(row=1, column=4, padx=5, pady=5)
        self.security_button = Tk.Button(master, text="Security", height=3, width=10, command=partial(self.buttonAction, 6))
        self.security_button.grid(row=1, column=5, padx=5, pady=5)
        self.transportation_button = Tk.Button(master, text="Transportation", height=3, width=10, command=partial(self.buttonAction, 7))
        self.transportation_button.grid(row=1, column=6, padx=5, pady=5)

        # message
        self.message = Tk.StringVar()
        Tk.Label(master, textvariable=self.message, bg='gray').grid(row=2, column=0, padx=5, pady=5, columnspan=7)

        # line plot
        # self.f = Figure(figsize=(6, 5), dpi=80)
        # self.ax0 = self.f.add_axes((.12, .1, .8, .85), axisbg=(.75, .75, .75), frameon=False)
        # self.ax0.set_xlabel('X Label')
        # self.ax0.set_ylabel('Y Label')
        # self.ax0.plot(np.max(np.random.rand(100, 10) * 10, axis=1), "r-")
        #
        # self.frame.grid(row=3, column=1, padx=5, pady=15, columnspan=5)
        #
        # self.canvas = FigureCanvasTkAgg(self.f, master=self.frame)
        # self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        # self.canvas.show()

        # self.f = Figure(figsize=(6, 5), dpi=100)
        # ax = self.f.add_subplot(111)
        # data = (20, 35, 30, 35, 27)
        # ind = np.arange(5)  # x bars
        #
        # rects1 = ax.bar(ind, data, .5)
        # canvas = FigureCanvasTkAgg(self.f, master)
        # canvas.show()
        # canvas.get_tk_widget().grid(row=3, column=1, padx=5, pady=15, columnspan=5)

        # bar plot
        word_count = 10
        x = scipy.arange(word_count)
        y = scipy.array(range(word_count))
        f = pylab.figure()
        ax = f.add_axes([.1, .1, .8, .8])
        ax.bar(x, y, align='center')
        ax.set_xticks(x)
        ax.set_xticklabels( word_count*[''])
        canvas = FigureCanvasTkAgg(f, master)
        canvas.show()
        canvas.get_tk_widget().grid(row=3, column=0, padx=5, pady=15, columnspan=7)

        # toolbar at base of plot
        self.toolbar = NavigationToolbar2TkAgg(canvas, self.frame)
        self.toolbar.pack()
        self.toolbar.update()

    def buttonAction(self, num):
        """Calling the section of articles depending on the button pressed"""

        # Possible Selection
        catalog = {
            1: 'Business',
            2: 'Culture',
            3: 'Design',
            4: 'Gear',
            5: 'Science',
            6: 'Security',
            7: 'Transportation'
        }

        # Update GUI message
        self.message.set("Reading " + catalog[num])
        self.frame.update()

        # Read in the data
        read_section(num)
        print("Section Complete")
        self.message.set(catalog[num] + " section read successfully")

        # Filter and display the data
        

if __name__ == '__main__':
    root = Tk.Tk()
    app = Window(root)
    root.mainloop()
