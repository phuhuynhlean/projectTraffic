import matplotlib.pyplot as plt

# path_quoclo1    = ["loc01","quoclo1-buithanhkhiet","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58afea5dbd82540010390c4d&t=1667011700842"]
# path_vovankiet  = ["loc02","vovankiet-caovanlau","http://giaothong.hochiminhcity.gov.vn:80/render/ImageHandler.ashx?id=56de42f611f398ec0c481296&t=1666752019191"]
# path_cauphumi   = ["loc03","vochicong-cauphumi","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5aab1f852d266a0017e5afd4&t=1667013794895"]
# path_binhtrieu  = ["loc04","quoclo13-phamvandong","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58affc6017139d0010f35cc8"]
# path_caotocLTDG = ["loc05"1,"caotocLTDG-doxuanhop","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5d9de43b766c880017188cb6&t=1667014633438"]
# path_quoclo22   = ["loc06","quoclo22-giaphai","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=589b4379b3bf7600110283c9"]
# path_binhphuoc  = ["loc07","quoclo13-quoclo1","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5874656eb807da0011e33cde&t=1667015665586"]
# path_linhxuan   = ["loc08","khavancan-quoclo1","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58746314b807da0011e33cce&t=1667015860315"]
# path_vothisau   = ["loc09","vothisau-dinhtienhoang","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5a823e425058170011f6eaa4"]

# f = open('runs/detect/01-11.txt', 'r')
# f = open('runs/detect/31-10.txt','r')
f = open('runs/detect/30-10.txt','r')

def sum(array):
  result = 0
  for i in range(0,len(array)):
    result += array[0]
  return result

cars = []
giants = []
bikes = []
# time_now = -1
for i in range(0,9):
  cars.append(0)
  giants.append(0)
  bikes.append(0)

for line in f:
  x = line.split()
  count = 0
  temp = ""
  index = -1

  meta = x[0]
  location = meta.split('-')[0]
  time = meta.split('-')[1]
  time = time.split('.')[0]
  time = time.split('_')
  # if (location != "loc09"):
  #   continue

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

x = [i+8 for i in range(0,len(cars))]
# print(x)
print(sum(cars))
print(sum(giants))
print(sum(bikes))

plt.xlabel('Time (hour)')
plt.ylabel('Vehicles (unit)')
plt.plot(x,cars, label = "Cars")
plt.plot(x,giants, label = "Giants")
plt.plot(x,bikes, label = "Bikes")
plt.title("Distribution of vehicles")
plt.legend()
plt.show()