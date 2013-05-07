from tkinter import *
from tkinter.messagebox import showinfo

def reply():
	showinfo(title='What is this?', message='Tkinter Python GUI, jaknow.')

def no():
	showinfo(title='Windows??', message='No No No! You are a nerd - you should not want to see that sun.')

window = Tk()

alert = Button(window, text='What is this?', command=reply)
windows = Button(window, text='Can we have windows?', command=no)
kranichs = Label(text="tkinter Example")

kranichs.pack()
alert.pack()
windows.pack()

window.mainloop()