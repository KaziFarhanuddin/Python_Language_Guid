from tkinter import *

root = Tk()

Entry(root, width=25).pack()
Button(root, width=25, text="Button").pack()
Checkbutton(root, text="Remember me").pack()
Label(text="This is a label").pack()
OptionMenu(root, IntVar(), "Sellect age", "10", "12", "15", '17', '19').pack()
Scrollbar(root, orient=VERTICAL).pack()
Radiobutton(root, text="Something", variable=IntVar(), value=3).pack()
Radiobutton(root, text="Anotherthing", variable=IntVar(), value=5).pack()

root.mainloop()
