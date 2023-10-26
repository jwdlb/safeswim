from .ImportWeatherConditions import *
from .ImportTides import *
from .SafeOrNot import SafeOrNot
from flask import Blueprint, render_template, request, flash

WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp = metDataInfoATM("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354690?res=3hourly&key=04b3e890-f695-43cb-bb72-fecc450c9b7e")
metDataInfoATM = ("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354690?res=3hourly&key=04b3e890-f695-43cb-bb72-fecc450c9b7e")

def SwWaWa(pBeach):
    swimming = True
    wading = True
    watersport = True
    temporary = []
    temporary.append(SafeOrNot.BigWavesOrNot(pBeach))
    temporary.append(SafeOrNot.temperature(pBeach))
    temporary.append(SafeOrNot.waterDirectionSafety(pBeach))
    temporary.append(SafeOrNot.extra(pBeach))
    if temporary[3][0] == False:
        swimming = False
    if temporary[3][1] == False:
        wading = False
    if temporary[3][2] == False:
        watersport = False
    return swimming,wading,watersport




auth = Blueprint('auth', __name__)

@auth.route('/coastline')
def coastline():
    return render_template("home.html")

@auth.route('/Specific_Beach_Information')
def login():
    return render_template("Specific Beach information.html")

@auth.route('/General_Beach_Information', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
    return render_template("General Beach information.html")

@auth.route('/Beach1')
def Beach1():
    #BeachName,currentDirectionBr,currentDirectionBh,currentTidalRate,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,RainProbATM,MaxUvIndexATM,SeaTemp,Watersport = True,Swimming= True,Wading=True):
    beach1SON  = SafeOrNot("Beach1",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach1SON)
    return render_template("Beach1.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach2')
def Beach2():
    beach2SON  = SafeOrNot("Beach2",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach2SON)
    return render_template("Beach2.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach3')
def Beach3():
    beach3SON  = SafeOrNot("Beach3",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach3SON)
    return render_template("Beach3.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach4')
def Beach4():
    beach4SON  = SafeOrNot("Beach4",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach4SON)
    return render_template("Beach4.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach5')
def Beach5():
    beach5SON  = SafeOrNot("Beach5",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach5SON)
    return render_template("Beach5.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach6')
def Beach6():
    beach6SON  = SafeOrNot("Beach6",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach6SON)
    return render_template("Beach6.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach7')
def Beach7():
    beach7SON  = SafeOrNot("Beach7",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach7SON)
    return render_template("Beach7.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach8')
def Beach8():
    beach8SON  = SafeOrNot("Beach8",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach8SON)
    return render_template("Beach8.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach9')
def Beach9():
    beach9SON  = SafeOrNot("Beach9",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach9SON)
    return render_template("Beach9.html", swimming=swimming, watersports = watersports, wading=wading)

@auth.route('/Beach10')
def Beach10():
    beach10SON  = SafeOrNot("Beach10",currentDirectionBr,currentDirectionBh,currentTidalRateBr,currentTidalRateBh,WindSpeedATM,AirTemperatureATM,AirFeelsLikeTempATM,VisibilityATM,WindDirectionATM,WeatherType,MaxUvIndexATM,SeaTemp)
    swimming,wading,watersports = SwWaWa(beach10SON)
    return render_template("Beach10.html", swimming=swimming, watersports = watersports, wading=wading)