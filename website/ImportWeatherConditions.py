#importing libaries
import json
import pandas as pd
import requests
import time


#Global variables
METDATAURL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354690?res=3hourly&key=04b3e890-f695-43cb-bb72-fecc450c9b7e"

#Fetches Weather data needed in safety calculations
def metDataInfoATM(pMETDATAURL):
    index = 0
    compassCode = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW",]
    bearing = [22,45,67,90,112,135,157,180,202,225,247,270,292,315,337]
    calender = [31,28,31,30,31,30,31,31,30,31,30,31]
    SeaTempList = [8.7,8.5,8,9.6,11.6,13.8,15.6,17.3,17.4,16.3,14.5,11.6]
    current_time = time.strftime("%m/%d/%y")
    month = int(current_time[0:2])
    day = int(current_time[3:5])
    fraction = (day)/calender[month-1]
    SeaTemp = SeaTempList[month-1] + (fraction*(SeaTempList[month]-SeaTempList[month-1]))
    metDataResponse = requests.get(pMETDATAURL)
    metData = metDataResponse.text
    jMetData = json.loads(metData)
    #print(jMetData)
    WindSpeedATM = int(jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["S"])
    AirTemperatureATM = int(jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["T"])
    AirFeelsLikeTempATM = int(jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["F"])
    VisibilityATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["V"]
    WindDirectionATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["D"]
    WeatherType = int(jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["W"])
    MaxUvIndexATM = int(jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["U"])
    for i in compassCode:
        if i == WindDirectionATM:

            WindDirectionATM = bearing[index-1]
        index += 1
    return WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp
metDataInfoATM(METDATAURL)

