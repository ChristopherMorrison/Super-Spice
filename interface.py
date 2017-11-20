from tkinter import *
# from matplotlib import *
# matplotlib.use("TkAgg")

# https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/

root = Tk()

def doNothing(event):
    print("Doing whatever this button wants")

def sendText(event):
    print("This will be a list of the most frequently used words for the selected topic")

title = Label(root, text="Wired.com")
title.grid(row=0, columnspan=7)

button_1 = Button(root, text="Business")
button_1.bind("<Button-1>", doNothing)
button_1.grid(row=1, padx=5, pady=5)

button_2 = Button(root, text="Culture")
button_2.bind("<Button-1>", doNothing)
button_2.grid(row=1, column=1, padx=5, pady=5)

button_3 = Button(root, text="Design")
button_3.bind("<Button-1>", doNothing)
button_3.grid(row=1, column=2, padx=5, pady=5)

button_4 = Button(root, text="Gear")
button_4.bind("<Button-1>", doNothing)
button_4.grid(row=1, column=3, padx=5, pady=5)

button_5 = Button(root, text="Science")
button_5.bind("<Button-1>", doNothing)
button_5.grid(row=1, column=4, padx=5, pady=5)

button_6 = Button(root, text="Security")
button_6.bind("<Button-1>", doNothing)
button_6.grid(row=1, column=5, padx=5, pady=5)

button_7 = Button(root, text="Transportation")
button_7.bind("<Button-1>", doNothing)
button_7.grid(row=1, column=6, padx=5, pady=5)



root.mainloop()
