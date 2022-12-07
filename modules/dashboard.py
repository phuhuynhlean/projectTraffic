from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import *
from PIL import Image, ImageTk
import PIL
import webbrowser

sidebar_color = '#00539C'
sidebar_text = 'white'
header_color = "#D2042D"
header_text = "white"
sidebar_y = 220
sidebar_x = 5

def callback(url):
    webbrowser.open_new(url)

class Dashboard:
    def __init__(self, window):
        self.window = window
        
        # tabControl = ttk.Notebook(window)
        
        # tab1=tk.Frame(tabControl, background="white")
        # tab2=tk.Frame(tabControl, background="white")

        # tabControl.add(tab1, text='Daily')
        # tabControl.add(tab2, text='Weekly')
        # tabControl.pack(expand=1, fill="both")

        # header
        self.header = Frame(self.window, bg=header_color)
        self.header.place(x = 300, y = 28, width = 2000, height = 120,)
        text = Label(text="Traffic Capture in Ho Chi Minh City", font=("Roboto", 25, "bold"), fg=header_text, background=header_color)
        text.place(x = 345, y = 65)


        # sidebar
        self.sidebar = Frame(self.window, bg =sidebar_color)
        self.sidebar.place(x = 0, y = 28, width = 300, height = 1500)
        image1 = Image.open("traffic/VGU.png")
        new_image1 = image1.resize((150, 150), PIL.Image.ANTIALIAS)
        test = ImageTk.PhotoImage(new_image1)
        label1 =Label(self.sidebar, image=test,borderwidth=0, relief="flat",background=sidebar_color,cursor="hand2")
        label1.image = test
        label1.pack(side=TOP,padx=20)
        label1.bind("<Button-1>", lambda e: callback("https://www.overleaf.com/read/rhrsbdsrhjfy"))
