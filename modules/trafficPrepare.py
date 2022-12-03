import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def sum(array):
  result = 0
  for i in range(0,len(array)):
    result += array[0]
  return result

def getTraffic(date, destination):
  f = open('traffic/'+date+'.txt','r')
  cars = []
  giants = []
  bikes = []
  for i in range(0,9):
    cars.append(0)
    giants.append(0)
    bikes.append(0)
  for line in f:
    x = line.split()
    temp = ""
    index = -1
    meta = x[0]
    location = meta.split('-')[0]
    time = meta.split('-')[1]
    time = time.split('.')[0]
    time = time.split('_')
    if (location != destination) and (destination != "all"):
      continue

    for i in range(0,len(time)):
      time[i] = int(time[i])

    if ( (time[3]>=8) and (time[3]<17)):
      index = time[3] - 8

    for part in x:
      if ("car" in part) or ("boat" in part):
        cars[index] += int(temp)
      if ("truck" in part) or ("bus" in part) or ("train" in part):
        giants[index] += int(temp)
      if ("motorcycle" in part) or ("bicycle" in part):
        bikes[index] += int(temp)
      temp = part
  # print(cars)
  # print(giants)
  # print(bikes)
  vehicles =[cars,giants,bikes]
  return vehicles

def getDate():
  date = []
  thisdir = os.getcwd()
  for r, d, f in os.walk(thisdir+"\\traffic"):
      for file in f:
          if file.endswith(".txt"):
              file = file.strip('.txt')
              file = '\t\t\t\t'+ file +'-2022'+'\t\t\t\t'
              date.append(file)
  return date

locationDict = {
  "Highway A1 - Long An":"loc01",
  "Highway 22 - Tay Ninh":"loc06",
  "Vo Van Kiet - District 5":"loc02",
  "Cau Bong Intersection":"loc09",
  "Binh Trieu Intersection":"loc04",
  "Binh Phuoc Intersection":"loc07",
  "Linh Xuan Intersection":"loc08",
  "Phu Mi Bridge ":"loc03",
  "Long Thanh - Dau Giay":"loc05",
  "all locations":"all"
}