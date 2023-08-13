import time
import pandas as pd
import requests
import json

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

#Formats Database into pandas data frame
def FormatDatabase(pDatabase):
    return dataBase

#Finds time when High tide is
def HighTide(pHighTideUR):
    return highTideTime

#Finds Users time difference to High tide
def DifferenceInTime(pHightide):
    return differenceInTime

#Searches data base for Spring and Neap tidal direction and rate for that Hour
def SearchForSpringAndNeap(pDifferenceInTime,pDataBase):
    return currentDirection, springRate, neapRate

#Finds when closest Spring and Neap Tides are
def ClosestSpringAndNeap(pSpringAndNeapURL):
    return spring, neap

#intrapolates spring tide dates and neap tide dates comapred to current date to find current tidal rate
def CurrentTidalRate(pSpring,pNeap,pSpringRate,pNeapRate):
    return currentTidalRate