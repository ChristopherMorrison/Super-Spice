import tkinter as Tk
from PIL import Image, ImageTk
from functools import partial
# from matplotlib import *
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

    # Download articles
    read_section(num)
    print("Section Complete")
    message.set(catalog[num] + " section read successfully")
    frame.update()

    # Data Filtering
    message.set("Filtering results...")
    word_list = Filter_File("./article.txt")
    frame.update()

    # Update Bar graph and frame
    message.set("Displaying results...")
    frame.update()

    # global bar_chart_axes
    xlabels = list(word_list.keys())
    yvals = list(word_list.values())

    # print(xlabels)
    # print(yvals)

    message.set("Finished")
    frame.update()
    main(False, xlabels, yvals)


def main(default=True, xlabels=None, yvals=None):
    # create a frame
    global frame
    frame = Tk.Frame()

    # clear text file
    clear_file()

    # title and background color and window size
    root.title('Wired.com Trends')
    root.configure(background='gray')
    root.geometry('810x950')

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
        btn = Tk.Button(root, text=Labels[i], height=3, width=13, command=partial(buttonAction, i + 1))
        btn.grid(row=1, column=i, padx=5, pady=10)

    # creates a changable message label in the row below the buttons.
    if default:
        global message
        message = Tk.StringVar()
        Tk.Label(root, textvariable=message, bg='gray').grid(row=2, column=0, padx=5, pady=5, columnspan=7)

    # bar graph
    words = 7
    x = range(words)
    y = range(words)
    f = pylab.figure(figsize=(8, 7))

    default_labels = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7']

    bar_chart_axes = f.add_axes([.1, .1, .9, .9])
    if default == True:
        bar_chart_axes.bar(x, y, align='center')
        bar_chart_axes.set_xticks(x)
        bar_chart_axes.set_xticklabels(default_labels)
    else:
        bar_chart_axes.bar(x, yvals, align='center')
        bar_chart_axes.set_xticks(x)
        bar_chart_axes.set_xticklabels(xlabels)
        pylab.xlabel('Most common words')
        pylab.ylabel('Word frequency')
    canvas = FigureCanvasTkAgg(f, root)
    canvas.show()
    canvas.get_tk_widget().grid(row=3, column=0, padx=5, pady=15, columnspan=7)
    frame.update()

    root.mainloop()


message = None
frame = None
root = Tk.Tk()  # initialize a window
main()
