import time
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime

#Global variables
dataBase = []
highTideTime = 0
differenceInTime = 0
currentDirection = 0
springRate = 0
neapRate = 0
spring = 0
neap = 0
currentTidalRate = 0.0
calender = [31,28,31,30,31,30,31,31,30,31,30,31]

tideDataFile = "D:\College work\Computer Science\Coursework\ss\website\TidesDatabase1.csv"
TIDEDATAURL = "http://www.worldtides.info/api/v3?heights&extremes&date=2023-08-22&lat=50.82838&lon=-0.13947&days=7&key=9e50d987-5931-442f-bed5-e61f006436e4"

#Formats Database into pandas data frame
def FormatDatabase(pDatabase):
    dataBase = pd.read_csv(pDatabase)
    #print(dataBase)
    return dataBase
#print(FormatDatabase(tideDataFile))

#Finds time when High tide is
def HighTide(pHighTideURL):
    highTideTime = []
    tideDataResponse = requests.get(pHighTideURL)
    tideData = tideDataResponse.text
    jTideData = json.loads(tideData)
    for i in (jTideData["extremes"]):
        if i["type"] == "High":
            highTideTime.append(str(i["date"]))
    highTideTime = int(highTideTime[0][11:13])
    return highTideTime

#Finds Users time difference to High tide
def DifferenceInTime(pHightide):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S")
    cHour = int(current_time[0:2])
    cMinute = int(current_time[3:5])
    differenceInTime = cHour - pHightide
    if differenceInTime < -6:
        differenceInTime += 12
        if differenceInTime < -6:
            differenceInTime += 12
    if differenceInTime > 6:
        differenceInTime -= 12
        if differenceInTime > 6:
            differenceInTime -= 12
    return differenceInTime
##DifferenceInTime(HighTide(TIDEDATAURL))

#Searches data base for Spring and Neap tidal direction and rate for that Hour
def SearchForSpringAndNeap(pDifferenceInTime,pDataBase):
    currentDirectionBr = pDataBase.loc[pDataBase["Hours Brighton"] == 0, "Tidal Stream direction (degrees)Br"]
    currentDirectionBh = pDataBase.loc[pDataBase["Hours Brighton"] == 0, "Tidal Stream direction (degrees)Bh"]
    springRateBr = pDataBase.loc[pDataBase["Hours Brighton"] == 0, "Tidal Rate at Spring Tides (knots)Br"]
    neapRateBr = pDataBase.loc[pDataBase["Hours Brighton"] == 0, "Tidal Rate at Neap Tides (knots)Br"]
    springRateBh = pDataBase.loc[pDataBase["Hours Brighton"] == 0, "Tidal Rate at Spring Tides (knots)Bh"]
    neapRateBh = pDataBase.loc[pDataBase["Hours Brighton"] == 0, "Tidal Rate at Neap Tides (knots)Bh"]
    currentDirectionBr = currentDirectionBr.item()
    currentDirectionBh = currentDirectionBh.item()
    springRateBr = springRateBr.item()
    neapRateBr = neapRateBr.item()
    springRateBh = springRateBh.item()
    neapRateBh = neapRateBh.item()
    return currentDirectionBr,currentDirectionBh, springRateBr ,springRateBh, neapRateBr ,neapRateBh
currentDirectionBr, currentDirectionBh, springRateBr ,springRateBh, neapRateBr ,neapRateBh = SearchForSpringAndNeap(DifferenceInTime(HighTide(TIDEDATAURL)),FormatDatabase(tideDataFile))



#Finds when closest Spring and Neap Tides are
def ClosestSpringAndNeap():
    spring = ""
    neap = ""
    t = time.localtime()
    current_time = time.strftime("%m/%d/%y")
    month = current_time[0:2]
    day = int(current_time[3:5])
    year = current_time[6:10]
    CalenderNS = [[["N","08/26/2023"],["S","09/02/2023"],["N","09/09/2023"],["S","09/17/2023"],["N","09/24/2023"],["S","10/01/2023"],["N","10/08/2023"],["S","10/16/2023"],["N","10/23/2023"],["S","10/30/2023"],["N","11/07/2023"],["S","11/15/2023"],["N","11/22/2023"],["S","11/28/2023"],["N","12/07/2023"],["S","12/14/2023"],["N","12/22/2023"],["S","12/29/2023"]],
                  [["N","01/06/2024"],["S","01/14/2024"],["N","01/21/2024"],["S","01/27/2024"],["N","02/04/2024"],["S","02/12/2024"],["N","02/19/2024"],["S","02/26/2024"]]]
    for year1 in CalenderNS:
        index = 0
        for date in year1:
            if year == date[1][8:10]:
                if month == date[1][0:2]:
                    if day >= int(date[1][3:5]):
                        if date[0] == "N":
                            neap = date[1]
                            spring = year1[index+1][1]
        index += 1
    return spring, neap
spring,neap = ClosestSpringAndNeap()
#intrapolates spring tide dates and neap tide dates comapred to current date to find current tidal rate
def CurrentTidalRate(pSpring,pNeap,pSpringRateBr,pSpringRateBh,pNeapRateBr,pNeapRateBh,pCalender):
    calenderLocal = calender
    t = time.localtime()
    current_time = time.strftime("%m/%d/%y")
    month = int(current_time[0:2])
    day = int(current_time[3:5])
    year = int(current_time[6:9])
    if (year% 4) == 0:
        calenderLocal = calenderLocal[1] + 1
    if int(pNeap[0:2]) != month:
        diffNeap = (calenderLocal[month - 1] - day) + int(pNeap[3:5])
    else:
        diffNeap = abs(int(pNeap[3:5]) - day)
    if int(pSpring[0:2]) != month:
        diffSpring = (calenderLocal[month - 1] - day) + int(pSpring[3:5])
    else:
        diffSpring = abs(int(pSpring[3:5]) - day)
    fraction = diffNeap/(diffNeap+diffSpring)
    currentTidalRateBr = pNeapRateBr + (fraction * (pSpringRateBr - pNeapRateBr))
    currentTidalRateBh = pNeapRateBh + (fraction * (pSpringRateBh - pNeapRateBh))
    return currentTidalRateBr, currentTidalRateBh
currentTidalRateBr,currentTidalRateBh = CurrentTidalRate(spring,neap,springRateBr ,springRateBh, neapRateBr ,neapRateBh,calender)

