#Import stuff here
import tkinter as tk

#Create instance
win = tk.Tk()

#Add title to GUI
win.title("Test GUI")

#Other properties of GUI
#win.resizable(False,False)#do you want it to be resizeable? x axis, y axis
coolFrame = tk.Frame(win)
coolFrame.pack()

#Widgets template is tk[widgetname](root window, properties/configuration)
tk.Label(coolFrame, text="this is the first label").pack()
tk.Button(coolFrame, text="Hi I'm a button").pack()

label2 = tk.Label(win, text="Label 2") #this is a label as a variable

#Start the GUI/Create the main loop
win.mainloop()