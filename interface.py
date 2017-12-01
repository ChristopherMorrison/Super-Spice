import tkinter as Tk
from PIL import Image, ImageTk
from functools import partial
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import numpy as np
from web_scrape import *
import matplotlib.pyplot as plt
import pylab


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


root = Tk.Tk()  # initialize a window

frame = Tk.Frame()  # create a frame

root.title('Wired.com Trends')  # title and background color
root.configure(background='gray')

img = Image.open(".\wired.jpg")  # insert picture at the top
img = img.resize((250, 50), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

imgLabel = Tk.Label(image=photo)
imgLabel.grid(row=0, columnspan=7)  # extends all 7 columns

# creates buttons for each section of wired.com
# when pressed, sends a value to the buttonAction function
business_button = Tk.Button(root, text="Business", height=3, width=10, command=partial(buttonAction, 1))
business_button.grid(row=1, column=0, padx=5, pady=5)
culture_button = Tk.Button(root, text="Culture", height=3, width=10, command=partial(buttonAction, 2))
culture_button.grid(row=1, column=1, padx=5, pady=5)
design_button = Tk.Button(root, text="Design", height=3, width=10, command=partial(buttonAction, 3))
design_button.grid(row=1, column=2, padx=5, pady=5)
gear_button = Tk.Button(root, text="Gear", height=3, width=10, command=partial(buttonAction, 4))
gear_button.grid(row=1, column=3, padx=5, pady=5)
science_button = Tk.Button(root, text="Science", height=3, width=10, command=partial(buttonAction, 5))
science_button.grid(row=1, column=4, padx=5, pady=5)
security_button = Tk.Button(root, text="Security", height=3, width=10, command=partial(buttonAction, 6))
security_button.grid(row=1, column=5, padx=5, pady=5)
transportation_button = Tk.Button(root, text="Transportation", height=3, width=10, command=partial(buttonAction, 7))
transportation_button.grid(row=1, column=6, padx=5, pady=5)

# creates a changable message label in the row below the buttons.
message = Tk.StringVar()
Tk.Label(root, textvariable=message, bg='gray').grid(row=2, column=0, padx=5, pady=5, columnspan=7)


# bar graph
x = range(7)
y = [4, 7, 6, 5, 8, 11, 1]
f = pylab.figure()
ax = f.add_axes([.1, .1, .8, .8])
ax.bar(x, y, align='center')
ax.set_xticks(x)
ax.set_xticklabels(['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7'])
canvas = FigureCanvasTkAgg(f, root)
canvas.show()
canvas.get_tk_widget().grid(row=3, column=0, padx=5, pady=15, columnspan=7)

# adds tool bar below the graph
toolbar = NavigationToolbar2TkAgg(canvas, frame)
toolbar.pack()
toolbar.update()

root.mainloop()
