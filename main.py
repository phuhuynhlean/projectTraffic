import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ctypes import windll
from modules.trafficPrepare import *
from modules.dashboard import *
from modules.analyzer import *
import numpy as np
from PIL import Image, ImageTk
import PIL

def init_window():
  windll.shcore.SetProcessDpiAwareness(1)

  #Start window (User Interface - UI)
  window = tk.Tk()

  window.title("Traffic App")
  window.geometry("1050x950")
  window.configure(bg='white')
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
  figure1 = plt.Figure(figsize=(6,6), dpi=100)
  
  figure1.clf()
  ax1 = figure1.add_subplot(111)
  label = ['08:00\n-9:00', '09:00\n-10:00', '10:00\n-11:00', '11:00\n-12:00', '12:00\n-13:00','13:00\n-14:00','14:00\n-15:00','15:00\n-16:00','16:00\n-17:00']
  traffic_data = getTraffic(date,destination)
  car = traffic_data[0];  giant = traffic_data[1];  bike = traffic_data[2]
  df1_data = {'time': label, 'bike': bike, 'car': car, 'giant': giant } 
  df1 = pd.DataFrame(df1_data)

  graph = FigureCanvasTkAgg(figure1, window)
  graph_pointer = graph.get_tk_widget()
  graph_pointer.place(x=310,y=150)
  df1 = df1[['time', 'bike','car','giant']].groupby('time').sum().plot(kind='line', ax=ax1)
  ax1.set_ylim(ymin=0, ymax = max(max(bike),max(giant),max(car))*1.1)
  
  for i in locationDict:
    if locationDict[i]==destination:
      locationTxt=i
  print(locationTxt)
  ax1.set_title('Traffic at '+ locationTxt + " ["+ date+"]")
  count = 1
  print(traffic_data)
  analysisTxt = data_analyzing(traffic_data)
  text = Text(window, padx=15, pady=15,height=20, width=25,bg= sidebar_color, fg= sidebar_text, font=("Times New Roman",12))
  text.config(bd = 3)
  text.insert('1.0', analysisTxt)
  text.place(x=5, y=450)

def get_content(entry):
    content=entry.get()
    return str(content)

def onClick():
    date = get_content(clicked_date).strip('\t')
    date = date.strip('-2022')
    loc = get_content(clicked_loc)
    loc = locationDict[loc]

    graphTraffic(date,loc) 


window = init_window()
ax1 = 0
count = 0
graph_pointer = 0

dashboard = Dashboard(window)
location = list(locationDict.keys())
date = getDate()

label_date = tk.Label(text="Date: ",bg=sidebar_color,fg=sidebar_text,anchor="e")
label_date.place(x=sidebar_x,y=sidebar_y,width=70,height=30)

clicked_date = StringVar()
clicked_date.set('Select the date')
drop_date = OptionMenu(window,clicked_date,*date)
drop_date.place(x=sidebar_x+70,y=sidebar_y,width = 200,height=30)

label_loc = tk.Label(text="Area: ",bg=sidebar_color,fg=sidebar_text,anchor="e")
label_loc.place(x=sidebar_x,y=sidebar_y+50,width=70,height=30)

clicked_loc = StringVar(window)
clicked_loc.set('Select the location')
drop_loc = OptionMenu(window,clicked_loc,*location)
drop_loc.place(x=sidebar_x+70,y=sidebar_y+50,width = 200,height=30)

button = tk.Button(text = "Graph", command= onClick, cursor="hand2")
button.place(x=sidebar_x +70,y=sidebar_y+95,width=200,height=45)
graphTraffic("12-11","all")

window.mainloop()
