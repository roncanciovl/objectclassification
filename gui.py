from tkinter import *
import tkinter as tk
 
root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Robot GUI")
label.pack()
 
button1 = Button(leftframe, text = "Start")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Stop")
button2.pack(padx = 3, pady = 3)
button3 = Button(leftframe, text = "Pause")
button3.pack(padx = 3, pady = 3)

#comment ctl + C + k

# frame = Frame(root, bd = 5, bg = "purple")
# frame.pack()
 
# leftframe = Frame(root, bg = "blue", bd = 3)
# leftframe.pack(side=LEFT)
 
# rightframe = Frame(root, bg = "red", bd = 3)
# rightframe.pack(side=RIGHT)


class Window:
    def __init__(self, master):
         
        label_frame = tk.LabelFrame(master, text = "Objeto")
        label_frame.pack(padx = 5, pady = 5)
 
        var = tk.IntVar()
 
        radio1 = tk.Radiobutton(label_frame, text = "Botella",
                                variable = var, value = 1)
        radio1.pack(padx = 5, pady = 5)
 
        radio2 = tk.Radiobutton(label_frame, text = "Lata",
                                variable = var, value = 2)
        radio2.pack(padx = 5, pady = 5)
 
        radio3 = tk.Radiobutton(label_frame, text = "Otro",
                                variable = var, value = 3)
        radio3.pack(padx = 5, pady = 5)
 
 
Window(root)
 
root.title("GUI")
root.mainloop()