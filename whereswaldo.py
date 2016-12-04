import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
width = 0
height = 0


class waldo(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        tk.Tk.wm_title(self,"Wheres Waldo")
        container.pack(side = "top", fill  = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}


        xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)

        yscrollbar = Scrollbar(self)
        yscrollbar.pack( side = RIGHT, fill=Y )



        f = StartPage
        frame = f(container, self)

        self.frames[f] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()




class StartPage(tk.Frame):

    def __init__(self,parent,master):

        global width,height
        tk.Frame.__init__(self,parent)

        image = Image.open("/Users/jasonfitzgerald/Desktop/FreeTime/hackathon/whereswaldo-master/waldo_dinosaurs.png")
        photo = ImageTk.PhotoImage(image)
        nextButton = Button(self,text="Hint")
        nextButton.pack(side = TOP)

        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.pack(side = BOTTOM)

        # sb = Scrollbar(self,orient = VERTICAL)
        # sb.pack(side=LEFT,fill=Y)


        # waldo1 = Image.open("swamp_waldo.jpg")
        # waldo2 = Image.open("waldo_dinosaurs.jpg")
        # waldo3 = Image.open("waldo_store.jpg")
        # waldo4 = Image.open("waldo_streets.jpg")
        # waldo5 = Image.open("waldo_wizards.jpg")
        # waldo6 = Image.open("maps_troy_waldo")
        #
        # waldo1.load()
        # waldo2.load()
        # waldo3.load()
        # waldo4.load()
        # waldo5.load()
        # waldo6.load()
        #
        #
        #
        # waldo6.show()


app = waldo()
app.geometry("2000x2000")
# app.resizable(width=False, height=False)
app.mainloop()
