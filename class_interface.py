import tkinter as Tk
from PIL import Image, ImageTk
from functools import partial
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from web_scrape import *

class Window():
    def __init__(self, master):
        self.frame = Tk.Frame(master)

        self.img = Image.open("wired.jpg")
        # self.img = Image.open("D:\programming\PythonClassFiles\project\Super-Spice\wired.jpg")  #for my end
        self.img = self.img.resize((250, 50), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)

        self.imgLabel = Tk.Label(image=self.photo)
        self.imgLabel.grid(row=0, columnspan=7)

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

        self.message = Tk.StringVar()
        Tk.Label(master, textvariable=self.message, bg='gray').grid(row = 2, column=0, padx=5, pady=15, columnspan=7)

    def buttonAction(self, num):
        catalog = {
            1: 'Business',
            2: 'Culture',
            3: 'Design',
            4: 'Gear',
            5: 'Science',
            6: 'Security',
            7: 'Transportation'
        }
        if num == 1:
            self.message.set("Asked for " + catalog[num] + " section")
        elif num == 2:
            self.message.set("Asked for " + catalog[num] + " section")
        elif num == 3:
            self.message.set("Asked for " + catalog[num] + " section")
        elif num == 4:
            self.message.set("Asked for " + catalog[num] + " section")
        elif num == 5:
            self.message.set("Asked for " + catalog[num] + " section")
        elif num == 6:
            self.message.set("Asked for " + catalog[num] + " section")
        elif num == 7:
            self.message.set("Asked for " + catalog[num] + " section")
        else:
            self.message.set("...")

        read_section(num)
        print("Section Complete")
        self.message.set(catalog[num] + " section completed successfully")



if __name__ == '__main__':
    root = Tk.Tk()
    app = Window(root)
    root.title("Wired.com Trends")
    root.configure(background='gray')
    root.update()
    root.deiconify()
    root.mainloop()
