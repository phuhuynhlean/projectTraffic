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

  print(cars)
  print(giants)
  print(bikes)
  # for i in range(0,len(cars)):
  #   if cars[i] == 0:
  #     cars[i] = (cars[i-1]+cars[i+1])/2
  # for i in range(0,len(giants)):
  #   if giants[i] == 0:
  #     giants[i] = (giants[i-1]+giants[i+1])/2
  # for i in range(0,len(bikes)):
  #   if bikes[i] == 0:
  #     bikes[i] = (bikes[i-1]+bikes[i+1])/2
  vehicles =[cars,giants,bikes]
  return vehicles

def getDate():
  # Getting the current work directory (cwd)
  thisdir = os.getcwd()

  # r=root, d=directories, f = files
  for r, d, f in os.walk(thisdir+"\\traffic"):
      for file in f:
          if file.endswith(".txt"):
              print(file.strip('.txt'))

getDate()