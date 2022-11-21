from modules.trafficGraph import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ctypes import windll
import time

def init_window():
    windll.shcore.SetProcessDpiAwareness(1)
    #Start window (User Interface - UI)
    window = tk.Tk()
    window.configure(bg='white')
    window.title("Traffic App")
    window.geometry("1100x850")
    p1 = PhotoImage(file = 'traffic/traffic-app-icon.png')
    window.iconphoto(False, p1)
    return window

def graphTraffic(date,destination):
  global ax1
  global count
  global graph_pointer
  if (count == 1):
    ax1.clear()
    graph_pointer.destroy()
  figure1 = plt.Figure(figsize=(6,5), dpi=100)
  
  figure1.clf()
  ax1 = figure1.add_subplot(111)
  label = ['08:00\n-9:00', '09:00\n-10:00', '10:00\n-11:00', '11:00\n-12:00', '12:00\n-13:00','13:00\n-14:00','14:00\n-15:00','15:00\n-16:00','16:00\n-17:00']
  car = getTraffic(date, destination)[0]
  truck = getTraffic(date, destination)[1]
  bike = getTraffic(date, destination)[2]
  df1_data = {'time': label,  'bike': bike, 'car': car, 'giant': truck }
  df1 = pd.DataFrame(df1_data)
  print(df1)

  graph = FigureCanvasTkAgg(figure1, window)
  graph_pointer = graph.get_tk_widget()
  graph_pointer.pack(side=tk.RIGHT, fill=tk.BOTH,pady=100) 
  df1 = df1[['time', 'bike','car','giant']].groupby('time').sum()
  df1.plot(kind='line', legend=True, ax=ax1)
  maximum = max(max(bike),max(truck),max(car))
  ax1.set_ylim(ymin=0, ymax = maximum*1.1)
  ax1.set_title('Traffic at '+ locationDict[destination] + " ["+ date+"]")
  count = 1

def get_content(entry):
    content=entry.get()
    return str(content)

def onClick():
    date=get_content(clicked_date)
    loc=get_content(clicked_loc)
    graphTraffic(date,loc) 


window = init_window()
ax1 = 0
count = 0
graph_pointer = 0

# location option
location = list(locationDict.keys())
date = getDate()

title = tk.Label(text="Traffic Capture at Ho Chi Minh City", font=("Arial",24),bg='white',fg='#aa1111')
title.place(x=200, y = 40)

label_date = tk.Label(text="Date: ",bg="white",anchor="e")
label_date.place(x=5,y=155,width=90,height=30)

clicked_date = StringVar()
clicked_date.set('Select the date')
drop_date = tk.OptionMenu(window,clicked_date,*date)
drop_date.place(x=95,y=155,width = 200,height=30)

label_loc = tk.Label(text="Location: ",bg="white",anchor="e")
label_loc.place(x=5,y=205,width=90,height=30)

clicked_loc = StringVar(window)
clicked_loc.set('Select the location')
drop_loc = tk.OptionMenu(window,clicked_loc,*location)
drop_loc.place(x=95,y=205,width = 200,height=30)

button = tk.Button(text = "Graph", command= onClick )
button.place(x=95,y=255,width=200,height=30)
graphTraffic("12-11","all")

window.mainloop()
