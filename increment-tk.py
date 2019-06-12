#https://stackoverflow.com/questions/26598010/how-do-i-create-a-button-in-python-tkinter-to-increase-integer-variable-by-1-and
import tkinter
import sys

root = tkinter.Tk()
root.geometry("150x60")
root.title("His Button Increaser")

counter = tkinter.IntVar()

def onClick(event=None):
    counter.set(counter.get() + 1)

def nClick():
    counter.set(0)

tkinter.Label(root, textvariable=counter).pack()
tkinter.Button(root, text="Increase", command=onClick, fg="dark green", bg = "white").pack(side=tkinter.LEFT)
tkinter.Button(root, text="Reset", command=nClick, fg="dark green", bg = "white").pack(side=tkinter.LEFT)

root.mainloop()