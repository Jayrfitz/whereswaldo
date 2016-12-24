from tkinter import *
from PIL import Image, ImageTk, ImageDraw
root = Tk()
i = 0
folder = "/Users/jasonfitzgerald/Desktop/FreeTime/hackathon/whereswaldo-master/"

Tk.wm_title(root,"Wheres Waldo")
#Add a canvas to the window
canvas = Canvas(root,width=1000, height=1000)
canvas.grid(column=0, row=0, sticky=N+S+E+W)

#Allow the canvas (in row/column 0,0)
#to "grow" to fill the entire window.
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


#Add a scrollbar that will scroll the canvas vertically
vscrollbar = Scrollbar(root)
vscrollbar.grid(column=1, row=0, sticky=N+S)
#Link the scrollbar to the canvas
canvas.config(yscrollcommand=vscrollbar.set)
vscrollbar.config(command=canvas.yview)


#Add a scrollbar that will scroll the canvas horizontally
hscrollbar = Scrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(column=0, row=1, sticky=E+W)
canvas.config(xscrollcommand=hscrollbar.set)
hscrollbar.config(command=canvas.xview)



#This frame must be defined as a child of the canvas,
#even though we later add it as a window to the canvas
f = Frame(canvas)

def hint(image):
    global i
    global label
    i = i + 1
    label.grid_forget()
    if i == 1:
        image = Image.open(folder +"waldo_dinosaurs_hint1.png")
    if i == 2:
        image = Image.open(folder +"waldo_dinosaurs_hint2.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(f,image = photo)
    label.image = photo # keep a reference!
    label.grid(row=1, column=1)
    if i > 2:
        return

image = Image.open(folder +"waldo_dinosaurs.png")
photo = ImageTk.PhotoImage(image)
label = Label(f,image = photo)
label.image = photo # keep a reference!
label.grid(row=1, column=1)

#Create a button in the frame.
b = Button(f,text="Hint",command = lambda: hint(image))
b.grid(row=0, column=1)


#Add the frame to the canvas
canvas.create_window((0,0), anchor=NW, window=f)

#IMPORTANT:
f.update_idletasks() #REQUIRED: For f.bbox() below to work!

#Tell the canvas how big of a region it should scroll
canvas.config(scrollregion= f.bbox("all")  )

mainloop()  #Wait for user events!
