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
from modules.dashboard import *
import numpy as np
from PIL import Image, ImageTk
import PIL


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

  window.title("Traffic App")
  window.geometry("1050x950")
  window.configure(bg='white')
  p1 = PhotoImage(file = 'traffic/traffic-app-icon.png')
  window.iconphoto(False, p1)
  tabControl = ttk.Notebook(window)
  
  #image1
  image1 = PIL.Image.open("traffic/VGU.png")
  new_image1 = image1.resize((150, 150), PIL.Image.ANTIALIAS)
  test = ImageTk.PhotoImage(new_image1)

  label1 = ttk.Label(image=test)
  label1.image = test

  #Position image1
  label1.place(x=900, y=840)

  tab1=tk.Frame(tabControl, background="white")
  tab2=tk.Frame(tabControl, background="white")

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
  figure1 = plt.Figure(figsize=(6,6), dpi=100)
  
  figure1.clf()
  ax1 = figure1.add_subplot(111)
  label = ['08:00\n-9:00', '09:00\n-10:00', '10:00\n-11:00', '11:00\n-12:00', '12:00\n-13:00','13:00\n-14:00','14:00\n-15:00','15:00\n-16:00','16:00\n-17:00']
  car = getTraffic(date, destination)[0]
  truck = getTraffic(date, destination)[1]
  bike = getTraffic(date, destination)[2]
  df1_data = {'time': label, 'bike': bike, 'car': car, 'giant': truck } 
  df1 = pd.DataFrame(df1_data)
  print(df1)
  data_analyzing(date, destination)

  graph = FigureCanvasTkAgg(figure1, window)
  graph_pointer = graph.get_tk_widget()
  graph_pointer.place(x=310,y=90)
  df1 = df1[['time', 'bike','car','giant']].groupby('time').sum()
  df1.plot(kind='line', ax=ax1)
  maximum = max(max(bike),max(truck),max(car))
  ax1.set_ylim(ymin=0, ymax = maximum*1.1)
  ax1.set_title('Traffic at '+ locationDict[destination] + " ["+ date+"]")
  count = 1
  
  analytics = data_analyzing(date, destination)
  # analytics.place(x=310,y=500)
  sum_vehicles = ('Total: ' + str(sum(analytics[0])) + ' vehicles' +'\n'
  + 'Average: ' + str(int(round(analytics[1],-1)))+'\n'
  + 'Median: ' + str(int(round(analytics[2],-1))) + '\n'
  + 'Standard deviation:' + str(int(round(analytics[3],-1))) + '\n'
  # + 'The variance of this data is ' + str(int(round(analytics[4],-1))) + '\n'
  + 'Range:' + str(int(round(analytics[5],-1))) + '\n'
  + '75%' ' of the time vehicles is below ' + str(int(round(analytics[6],-1))) + '\n'
  )
  text = Text(window, bd = 0,height=50, width=80,font=("Helvetica", 14))
  text.insert('1.0', sum_vehicles)
  text.place(x=window.winfo_screenwidth()/21,y=5*window.winfo_screenheight()/7)


def data_analyzing(date, destination):

  car = getTraffic(date, destination)[0]
  truck = getTraffic(date, destination)[1]
  bike = getTraffic(date, destination)[2]
  all = list()

  for i,j,k in zip(car,truck,bike):
    all.append(i+j+k)

  # Mean: Average vehicles at any moment 
  car_Mean = np.mean(car)
  bike_Mean = np.mean(bike)
  truck_Mean = np.mean(truck)
  all_Mean = np.mean(all)
  Mean = [car_Mean, bike_Mean, truck_Mean, all_Mean]

  # Median: The middle value of the set of vehicles
  car_Median = np.median(car)
  bike_Median = np.median(bike)
  truck_Median = np.median(truck)
  all_Median = np.median(all)
  Median = [car_Median, bike_Median, truck_Median, all_Median]

  # Mode
  # car_Mode = max(set(car), key = car.count)
  # bike_Mode = max(set(bike), key = bike.count)
  # truck_Mode = max(set(truck), key = truck.count)
  # Mode = [car_Mode, bike_Mode, truck_Mode]

  # Standard Deviation: The amount of vehicles that varies from the mean.
  car_Std = np.std(car)
  bike_Std = np.std(bike)
  truck_Std = np.std(truck)
  all_Std = np.std(all)
  Std = [car_Std, bike_Std, truck_Std, all_Std]

  # Variance
  car_Var = np.var(car)
  bike_Var = np.var(bike)
  truck_Var = np.var(truck)
  all_Var = np.var(all)
  Var = [car_Var, bike_Var, truck_Var, all_Var]

  # Range: The difference between the highest and lowest number of vehicles
  car_Range = max(car) - min(car)
  bike_Range = max(bike) - min(bike)
  truck_Range = max(truck) - min(truck)
  all_Range = max(all) - min(all)
  Range = [car_Range, bike_Range, truck_Range, all_Range]

  # Percentile: 75% of the time the number of vehicles is less than this number
  car_Percentile = np.percentile(car, 75)
  bike_Percentile = np.percentile(bike, 75)
  truck_Percentile = np.percentile(truck, 75)
  all_Percentile = np.percentile(all, 75)
  Percentile = [car_Percentile, bike_Percentile, truck_Percentile, all_Percentile]

  # Correlation: The relationship between two variables
  # car_Correlation = np.corrcoef(car, truck)[1][0]
  # bike_Correlation = np.corrcoef(bike, truck)[1][0]
  # truck_Correlation = np.corrcoef(truck, truck)[1][0]
  # Correlation = [car_Correlation, bike_Correlation, truck_Correlation]
  one_list = [all,all_Mean, all_Median, all_Std, all_Var, all_Range, all_Percentile]
  return one_list


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

Dashboard(window)

# location option
location = list(locationDict.keys())
date = getDate()

# title = tk.Label(text="Traffic Capture at Ho Chi Minh City", font=("Roboto",25),bg='white',fg='#aa1111')
# title.place(x = 200, y = 40)
text = Label(text="Traffic Capture at Ho Chi Minh City", font=("Roboto", 25, "bold"), fg='red', background="white")
text.place(x = 220, y = 40)


label_date = tk.Label(text="Date: ",bg="white",anchor="w")
label_date.place(x=5,y=155,width=90,height=30)

clicked_date = StringVar()
clicked_date.set('Select the date')
drop_date = tk.OptionMenu(window,clicked_date,*date)
drop_date.place(x=95,y=155,width = 200,height=30)

label_loc = tk.Label(text="Location: ",bg="white",anchor="w")
label_loc.place(x=5,y=205,width=90,height=30)

clicked_loc = StringVar(window)
clicked_loc.set('Select the location')
drop_loc = tk.OptionMenu(window,clicked_loc,*location)
drop_loc.place(x=95,y=205,width = 200,height=30)

button = tk.Button(text = "Graph", command= onClick)
button.place(x=95,y=255,width=200,height=60)
graphTraffic("12-11","all")

window.mainloop()
