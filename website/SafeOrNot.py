class SafeOrNot():
    #specific dangers of a beach:[Name,Bearing of coastline]
    BeachProperties = [["Beach1",100],["Beach1",100],["Beach1",100],["Beach1",100],["Beach1",100],["Beach1",85],["Beach1",125],["Beach1",125],["Beach1",40],["Beach1",40]]
    def __init__(self,BeachName,currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp,Watersport = True,Swimming= True,Wading=True):
        self.WindSpeedATM = WindSpeedATM
        self.AirTemperatureATM = AirTemperatureATM
        self.AirFeelsLikeTempATM = AirFeelsLikeTempATM
        self.VisibilityATM = VisibilityATM
        self.WindDirectionATM = WindDirectionATM
        self.WeatherType = WeatherType
        self.MaxUvIndexATM = MaxUvIndexATM
        self.currentTidalRateBr = currentTidalRateBr
        self.currentTidalRateBh = currentTidalRateBh
        self.currentDirectionBr = currentDirectionBr
        self.currentDirectionBh = currentDirectionBh
        self.Wading = Wading
        self.Watersport = Watersport
        self.Swimming = Swimming
        self.SeaTemp = SeaTemp
        self.BeachName = BeachName

    #Determines if safe due to waves
    def BigWavesOrNot(self):
        if self.WindDirectionATM > 232 and self.WindDirectionATM < 254:
            if self.WindSpeedATM >  10:
                self.Swimming = False
            if self.WindSpeedATM > 16:
                self.Wading = False
            if self.WindSpeedATM > 30:
                self.Watersport = False
        else:
            if self.WindSpeedATM >  12:
                self.Swimming = False
            if self.WindSpeedATM > 20:
                self.Wading = False
            if self.WindSpeedATM > 35:
                self.Watersport = False
        return self.Swimming, self.Wading, self.Watersport

    #determines if safe in these sea and air temperatures
    def temperature(self):
    #Safe in this water temperature?
        if self.AirFeelsLikeTempATM < 12:
            self.Wading = False
            self.Swimming = False
        if self.AirFeelsLikeTempATM < 8:
            self.Watersport = False
    #Safe in this sea temperature?
        if self.SeaTemp < 14:
            self.Wading = False
            self.Swimming = False
        if self.SeaTemp < 12:
            self.Watersport = False
        return self.Swimming, self.Wading, self.Watersport

    #determines if safe due to tides + winds
    def waterDirectionSafety(self):
        #specific dangers of a beach:[Name,Bearing of coastline]
        BeachProperties = [["Beach1",100],["Beach1",100],["Beach1",100],["Beach1",100],["Beach1",100],["Beach1",85],["Beach1",125],["Beach1",125],["Beach1",40],["Beach1",40]]
        if len(self.BeachName) == 6:
            if int(self.BeachName[5]) < 6:
                seaDirection = self.currentDirectionBr
                seaSpeed = self.currentTidalRateBr
            else:
                seaDirection = self.currentDirectionBh
                seaSpeed = self.currentTidalRateBh
        else:
            seaDirection = self.currentDirectionBh
            seaSpeed = self.currentTidalRateBh
        diff = abs(self.WindDirectionATM - seaDirection)
        if diff < 90:
            diff = 90-diff
            diff = diff/90
            seaSpeed = seaSpeed + diff*(self.WindSpeedATM/10)
        for i in BeachProperties:
            if i[0] == self.BeachName:
                if seaDirection > i[1] and seaDirection < i[1]:
                    if seaSpeed > 1.4:
                        self.Wading = False
                        self.Swimming = False
                        self.Watersport = False
                else:
                    if seaSpeed > 0.8:
                        self.Wading = False
                        self.Swimming = False
                    if seaSpeed > 1:
                        self.Watersport = False

        return self.Swimming, self.Wading, self.Watersport

    #determines if safe due to extra conditions
    def extra(self):
        if self.VisibilityATM == "VP" or self.VisibilityATM == "PO":
            print("hi")
            self.Swimming = False
            self.Watersport = False
            self.Wading = False
        if self.MaxUvIndexATM >= 9:
            print("hq")
            self.Swimming = False
            self.Watersport = False
            self.Wading = False
        return self.Swimming, self.Wading, self.Watersport











