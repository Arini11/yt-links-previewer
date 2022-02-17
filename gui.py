from tkinter import *

# create root window
import Main2

root = Tk()
root.title("YT Links")
root.geometry('500x250')

# Label
titol = Label(root, text="")
titol.grid(column=1, row=3)

# TextBox
link = Entry(root, width=75)
link.grid(column=1, row=1)


# OnKeyDownReturn
def enter(event):
    res = Main2.getTitol(link.get())
    titol.configure(text=res)


root.bind("<Return>", enter)

# Execute Tkinter
root.mainloop()
