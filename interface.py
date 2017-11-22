from tkinter import *
from PIL import Image, ImageTk
from functools import partial
# from matplotlib import *
# matplotlib.use("TkAgg")

# https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/

root = Tk()
root.title("Wired.com Trends")
root.configure(background="grey")

def doNothing(num):
    if num == 1:
        print("Passed in", num)
        return
    elif num == 2:
        print("Passed in", num)
        return
    elif num == 3:
        print("Passed in", num)
        return
    elif num == 4:
        print("Passed in", num)
        return
    elif num == 5:
        print("Passed in", num)
        return
    elif num == 6:
        print("Passed in", num)
        return
    elif num == 7:
        print("Passed in", num)
        return
    print("Doing whatever this button wants")

# title = Label(root, text="Wired.com", bg='grey')
# title.grid(row=0, columnspan=7)

# img = Image.open("wired.jpg")
img = Image.open("D:\PythonClassFiles\project\Super-Spice\wired.jpg")  #for my end
img = img.resize((250,50), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

imgLabel = Label(image=photo)
imgLabel.grid(row=0, columnspan=7)

button_1 = Button(root, text="Business", height=3, width=10, command=partial(doNothing,1))
# button_1.bind("<Button-1>", doNothing)
button_1.grid(row=1, column=0, padx=5, pady=5)

button_2 = Button(root, text="Culture", height=3, width=10, command=partial(doNothing,2))
# button_2.bind("<Button-1>", doNothing)
button_2.grid(row=1, column=1, padx=5, pady=5)

button_3 = Button(root, text="Design", height=3, width=10, command=partial(doNothing,3))
# button_3.bind("<Button-1>", doNothing)
button_3.grid(row=1, column=2, padx=5, pady=5)

button_4 = Button(root, text="Gear", height=3, width=10, command=partial(doNothing,4))
# button_4.bind("<Button-1>", doNothing)
button_4.grid(row=1, column=3, padx=5, pady=5)

button_5 = Button(root, text="Science", height=3, width=10, command=partial(doNothing,5))
# button_5.bind("<Button-1>", doNothing)
button_5.grid(row=1, column=4, padx=5, pady=5)

button_6 = Button(root, text="Security", height=3, width=10, command=partial(doNothing,6))
# button_6.bind("<Button-1>", doNothing)
button_6.grid(row=1, column=5, padx=5, pady=5)

button_7 = Button(root, text="Transportation", height=3, width=10, command=partial(doNothing,7))
# button_7.bind("<Button-1>", doNothing)
button_7.grid(row=1, column=6, padx=5, pady=5)

# f = Figure(figsize=(5,5), dpi=100)
# a = f.add_subplot(111)
# a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5]) #test plot
#
# canvas = FigureCanvasTkAgg(f, self)
# canvas.show()
# canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
#
# #optional toolbar
# toolbar = NavigationToolbar2TkAgg(canvas, self)
# toolbar.update()
# canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

root.mainloop()
