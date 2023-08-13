#importing libaries
import json
import pandas as pd
import requests


#Global variables
METDATAURL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354690?res=3hourly&key=04b3e890-f695-43cb-bb72-fecc450c9b7e"

#Fetches Weather data needed in safety calculations
def metDataInfoATM(pMETDATAURL):
    metDataResponse = requests.get(pMETDATAURL)
    metData = metDataResponse.text
    jMetData = json.loads(metData)
    WindSpeedATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["S"]
    AirTemperatureATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["T"]
    AirFeelsLikeTempATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["F"]
    VisibilityATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["V"]
    WindDirectionATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["D"]
    RainProbATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["Pp"]
    MaxUvIndexATM = jMetData["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["U"]
    print(WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,RainProbATM,MaxUvIndexATM)
metDataInfoATM(METDATAURL)

