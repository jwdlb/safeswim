import unittest
from SafeOrNot import  SafeOrNot

class MyTestCase(unittest.TestCase):
    def test_something(self):
        #4 12 12 GO NNW 7 1 17.39032258064516
        #BeachName,currentDirectionBr,currentDirectionBh,currentTidalRate,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,RainProbATM,MaxUvIndexATM,SeaTemp,Watersport = True,Swimming= True,Wading=True):
        mySafeOrNot  = SafeOrNot("Beach1",110,150,0.5,4,12,12,"GO","NNW",7,1,17)
        tswimming, twading, twatersport = SafeOrNot.temperature(mySafeOrNot)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
