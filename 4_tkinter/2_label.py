from tkinter import *

def main():
	print("You clicked me")

root = Tk()
root.geometry("300x200")

label = Label(text="This is a label")
label.grid(row=0, column=0)

btn = Button(text="click me", command=main)
btn.grid(row=0, column=1)

root.mainloop()