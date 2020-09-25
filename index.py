from tkinter import *
import os
import subprocess
import tkinter as tk
window = Tk()
window.title("Welcome to aptGUI")
window.geometry('225x80')
window.config(bg="#00bbc2")
package = tk.StringVar()
sudo = tk.StringVar()
txt = Entry(window,width=10,textvariable=package)
txt.grid(column=2, row=0)
def clicked():
    lbl = Label(window, text=package.get())
    lbl.grid(column=1, row=2)
    subprocess.call(["pkexec", "apt", "install", package.get(), "-y"])
def clicked1():
    subprocess.call(["pkexec", "apt","remove", package.get(), "-y"])
btn = Button(window, bg = "#42f498", text="run apt install", command=clicked)
btn.grid(column=1, row=0)
btn = Button(window, text="run apt remove", bg = "#42f498", command=clicked1)
btn.grid(column=1, row=1)
window.mainloop()


