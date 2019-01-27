from tkinter import *

def main(event):
	print("You clicked me")

root = Tk()
root.geometry("300x200")

label = Label(text="This is a label")
label.grid(row=0, column=0)

btn = Button(root, text="click me")
btn.grid(row=1, column=0)

# root.bind("<Button-1>", main)
btn.bind("<Button-1>", main)

root.mainloop()