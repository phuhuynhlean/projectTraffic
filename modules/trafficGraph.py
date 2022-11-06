import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# path_quoclo1    = ["loc01","quoclo1-buithanhkhiet","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58afea5dbd82540010390c4d&t=1667011700842"]
# path_vovankiet  = ["loc02","vovankiet-caovanlau","http://giaothong.hochiminhcity.gov.vn:80/render/ImageHandler.ashx?id=56de42f611f398ec0c481296&t=1666752019191"]
# path_cauphumi   = ["loc03","vochicong-cauphumi","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5aab1f852d266a0017e5afd4&t=1667013794895"]
# path_binhtrieu  = ["loc04","quoclo13-phamvandong","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58affc6017139d0010f35cc8"]
# path_caotocLTDG = ["loc05"1,"caotocLTDG-doxuanhop","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5d9de43b766c880017188cb6&t=1667014633438"]
# path_quoclo22   = ["loc06","quoclo22-giaphai","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=589b4379b3bf7600110283c9"]
# path_binhphuoc  = ["loc07","quoclo13-quoclo1","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5874656eb807da0011e33cde&t=1667015665586"]
# path_linhxuan   = ["loc08","khavancan-quoclo1","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58746314b807da0011e33cce&t=1667015860315"]
# path_vothisau   = ["loc09","vothisau-dinhtienhoang","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5a823e425058170011f6eaa4"]


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
  vehicles =[cars,giants,bikes]
  return vehicles

# a = getTraffic('31-10','loc08')
# print(a)