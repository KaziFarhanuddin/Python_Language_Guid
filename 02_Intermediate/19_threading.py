import threading
from tkinter import *
import time

def Sleep(event):
	btn = event.widget
	btn.config(text='Sleeping..') 
	time.sleep(2)
	btn.config(text='Awake') 

def Thread(event):
	thread_process = threading.Thread(target=Sleep, args=(event,))
	thread_process.start()

root = Tk()
btn = Button(text='Sleep 2sec')
btn.bind("<Button-1>", Thread)
btn.pack()
root.mainloop()
