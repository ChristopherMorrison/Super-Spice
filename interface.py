import tkinter as Tk
from PIL import Image, ImageTk
from functools import partial
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import pylab
from data_filter import *
from web_scrape import *


def buttonAction(num):
    """Calling the section of articles depending on the button pressed"""
    catalog = {
        1: 'Business',
        2: 'Culture',
        3: 'Design',
        4: 'Gear',
        5: 'Science',
        6: 'Security',
        7: 'Transportation'
    }
    message.set("Reading " + catalog[num])
    frame.update()

    read_section(num)
    print("Section Complete")
    message.set(catalog[num] + " section read successfully")


def main():
    # initialize a window
    root = Tk.Tk()

    # create a frame
    global frame
    frame = Tk.Frame()

    # title and background color
    root.title('Wired.com Trends')
    root.configure(background='gray')

    # insert picture at the top
    img = Image.open("./wired.jpg")
    img = img.resize((250, 50), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    imgLabel = Tk.Label(image=photo)
    imgLabel.grid(row=0, columnspan=7)  # extends all 7 columns

    # creates buttons for each section of wired.com
    # when pressed, sends a value to the buttonAction function
    Labels = ["Business", "Culture", "Design", "Gear", "Science", "Security", "Transportation"]
    for i in range(len(Labels)):
        btn = Tk.Button(root, text=Labels[i], height=3, width=10, command=partial(buttonAction, i + 1))
        btn.grid(row=1, column=i, padx=5, pady=5)

    # creates a changable message label in the row below the buttons.
    global message
    message = Tk.StringVar()
    Tk.Label(root, textvariable=message, bg='gray').grid(row=2, column=0, padx=5, pady=5, columnspan=7)

    # bar graph
    words = 7
    x = range(words)
    y = range(words)
    f = pylab.figure()
    ax = f.add_axes([.1, .1, .8, .8])
    ax.bar(x, y, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(['word'] * words)
    canvas = FigureCanvasTkAgg(f, root)
    canvas.show()
    canvas.get_tk_widget().grid(row=3, column=0, padx=5, pady=15, columnspan=7)

    # adds tool bar below the graph
    toolbar = NavigationToolbar2TkAgg(canvas, frame)
    toolbar.pack()
    toolbar.update()

    root.mainloop()


message = None
frame = None
main()
