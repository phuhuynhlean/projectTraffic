from numpy import *
from math import *

def data_analyzing(trafficData):
  name = ['Car','Giant','Bike']
  outputStr = "ANALYSIS\n\n"
  for i in range(0,3):
    total = str(sum(trafficData[i]))
    meanVal = str(floor(mean(trafficData[i])))
    stdVal = str(floor(std(trafficData[i])))
    maxVal = trafficData[i].index(max(trafficData[i])) + 8
    maxVal = str(maxVal) +":00 - " + str(maxVal+1)+":00"
    medianVal = trafficData[i].index(median(trafficData[i])) + 8
    medianVal = str(medianVal) +":00 - " + str(medianVal+1)+":00"
    # temp = 0; hour = 8
    # for j in trafficData[i]:
    #   temp += j
    #   if(2*temp >= int(total)):
    #     break
    #   hour +=1
    # medianVal = str(hour) +":00 - " + str(hour+1)+":00"
    outputStr += name[i] + ": " + total +" detected\n  Mean: " + meanVal + "\n  Std deviation: "+stdVal
    outputStr += "\n  Median:" + medianVal + "\n  Rush hour: "+maxVal+"\n\n"
  return outputStr