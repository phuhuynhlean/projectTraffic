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
import time
from modules.trafficGraph import *
import numpy as np

locationDict = {
  "loc01":"Highway A1 - Bui Thanh Khiet Intersection",
  "loc02":"Vo Van Kiet - Cao Van Lau Intersection",
  "loc03":"Phu Mi Bridge (Vo Chi Cong)",
  "loc04":"Binh Trieu Intersection (Highway 13)",
  "loc05":"Long Thanh - Dau Giay Expressway",
  "loc06":"Highway 22 - Gia Phai Intersection",
  "loc07":"Binh Phuoc Intersection (Highway 13)",
  "loc08":"Linh Xuan Intersection (Highway A1)",
  "loc09":"Cau Bong Intersection",
  "all":"all locations"
}

def init_window():
    windll.shcore.SetProcessDpiAwareness(1)
    #Start window (User Interface - UI)
    window = tk.Tk()
    window.configure(bg='white')
    window.title("Traffic App")
    window.geometry("1920x1200")
    p1 = PhotoImage(file = 'traffic/traffic-app-icon.png')
    window.iconphoto(False, p1)
    tabControl = ttk.Notebook(window)

    tab1=ttk.Frame(tabControl)
    tab2=ttk.Frame(tabControl)

    tabControl.add(tab1, text='Daily')
    tabControl.add(tab2, text='Weekly')
    tabControl.pack(expand=1, fill="both")


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
  data_analyzing(date, destination)

  graph = FigureCanvasTkAgg(figure1, window)
  graph_pointer = graph.get_tk_widget()
  graph_pointer.pack(side=tk.RIGHT, fill=tk.BOTH,pady=100) 
  df1 = df1[['time', 'bike','car','giant']].groupby('time').sum()
  df1.plot(kind='line', legend=True, ax=ax1)
  maximum = max(max(bike),max(truck),max(car))
  ax1.set_ylim(ymin=0, ymax = maximum*1.1)
  ax1.set_title('Traffic at '+ locationDict[destination] + " ["+ date+"]")
  count = 1
  text = Text(window, height=2, width=30)
  text.insert(INSERT,"Hello")
  text.place(x=window.winfo_screenwidth()/21,y=2*window.winfo_screenheight()/5)


def data_analyzing(date, destination):

  car = getTraffic(date, destination)[0]
  truck = getTraffic(date, destination)[1]
  bike = getTraffic(date, destination)[2]

  # Mean: Average vehicles at any moment 
  car_Mean = np.mean(car)
  bike_Mean = np.mean(bike)
  truck_Mean = np.mean(truck)
  Mean = [car_Mean, bike_Mean, truck_Mean]

  # Median: The middle value of the set of vehicles
  car_Median = np.median(car)
  bike_Median = np.median(bike)
  truck_Median = np.median(truck)
  Median = [car_Median, bike_Median, truck_Median]

  # Mode
  # car_Mode = max(set(car), key = car.count)
  # bike_Mode = max(set(bike), key = bike.count)
  # truck_Mode = max(set(truck), key = truck.count)
  # Mode = [car_Mode, bike_Mode, truck_Mode]

  # Standard Deviation: The amount of vehicles that varies from the mean.
  car_Std = np.std(car)
  bike_Std = np.std(bike)
  truck_Std = np.std(truck)
  Std = [car_Std, bike_Std, truck_Std]

  # Variance
  car_Var = np.var(car)
  bike_Var = np.var(bike)
  truck_Var = np.var(truck)
  Var = [car_Var, bike_Var, truck_Var]

  # Range: The difference between the highest and lowest number of vehicles
  car_Range = max(car) - min(car)
  bike_Range = max(bike) - min(bike)
  truck_Range = max(truck) - min(truck)
  Range = [car_Range, bike_Range, truck_Range]

  # Percentile: 75% of the time the number of vehicles is less than this number
  car_Percentile = np.percentile(car, 75)
  bike_Percentile = np.percentile(bike, 75)
  truck_Percentile = np.percentile(truck, 75)
  Percentile = [car_Percentile, bike_Percentile, truck_Percentile]

  # Correlation: The relationship between two variables
  # car_Correlation = np.corrcoef(car, truck)[1][0]
  # bike_Correlation = np.corrcoef(bike, truck)[1][0]
  # truck_Correlation = np.corrcoef(truck, truck)[1][0]
  # Correlation = [car_Correlation, bike_Correlation, truck_Correlation]
  print()


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
