import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyqrcode
import png
from pyqrcode import QRCode

top=tk.Tk()
name_var=tk.StringVar()
L1 = tk.Label(top, text="Enter URL")

L1.place(x=80,y=300)
E1 = tk.Entry(top,textvariable = name_var, bd =5)
E1.place(x=200,y=300)
top.geometry("700x700")

def helloCallBack():
    x=name_var.get()
    ur=pyqrcode.create(x)
    ur.png('link.png', scale=6)
    frame = Frame(top, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5) 
    mg = ImageTk.PhotoImage(Image.open("link.png"))
    label = Label(frame, image = mg)
    label.pack()

B = tk.Button(top, text ="Create QR code", command = helloCallBack)
B.place(x=300,y=400)
top.mainloop()