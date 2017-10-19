# Importerar funtionen som använder Google Maps Geocoding API
from geocoding_api import get_coordinates
# Importerar funktionen som använder SMHI's API
from smhi_api import get_weather_forecast
# Importerar funktionen som använder Spotify's API
from spotify_api import get_spotify_info
from flask import Flask
from flask import request
from flask import *

app = Flask(__name__)

@app.route('/')
def start():
    #visar startsidan där stad väljs, skickas vidare till route result
    return render_template("index.html")

@app.route('/result/', methods=['GET','POST'])
def find_city():
    # hämtar vilken stad som har angivits i formuläret
    city = request.form.get("city")
    # get_coordinates anropas med staden som argument för att ta fram koordinater
    # En lista innehållandes longitude och latitude returneras
    coordinates_list = get_coordinates(city)
    # get_weather_forecast anropas med koordinaterna som argument
    # En lista innehållandes temperatur och nuvarande vädersymbol returneras
    weather_forecast = get_weather_forecast(coordinates_list[0], coordinates_list[1])
    #tar ut endast vädersymbolen från weather_forecast.
    #SKa skickas till spotify och returneras i html result.
    weather_symbol = (weather_forecast['weather_symbol'])
    #tar ut endast temperaturen från weather_forecast
    #ska returneras till html result
    temp = (weather_forecast['temperature'])
    #JESSICA FÖRSTÅR EJ DENNA. VARFÖR HAR VI TVÅ CITY-VARIABLER? och vad gör city.title()?
    city = city.title()
    #get_spotify_info returnerar lista med alla artister, namnet på spellistan och länken till seplaren
    spotify_data = get_spotify_info(weather_symbol)
    #artists_in_a_playlist hämtar ut artisterna från spotify_data och sparar i en lista
    artists_in_a_playlist = spotify_data[0]
    #hämtar namnet på spellistan
    name_of_playlist = spotify_data[1]
    #playern för listan sparas i player
    player = spotify_data[2]

    #''' TA BORT DETTA SEN, ENDAST FÖR ATT VI SJÄLVA SKA SE ATT ALLT OVANSTÅENDE FUNGERAR'''
    #Först skrivs staden ut, sedan longitude och latitude. fungerar allt?
    print('*** ' + city.upper() + ' ***')
    print('*'*15)
    print('Longitude: ' + coordinates_list[0] + ' Latitude: ' + coordinates_list[1])
    #Skriver ut vår dictionary weather_forecast.
    print(weather_forecast)
    #kontrollerar att allt i dictionary weather_forecast stämmer.
    for i in weather_forecast:
        print(i + ': ' + str(weather_forecast[i]))
    #kontrollera att vädersymbolen är korrekt i variabeln weather_symbol
    print(weather_symbol)
    #kontrollera är temperaturen är korrekt i variabeln temp
    print(temp)
    #testar att name_of_playlist innehåller korrekt namn på spellista
    #samt att alla artister finns sparade i artists_in_a_playlist
    #även att player kan spela upp listan!
    print("We found this playlist for you: " + name_of_playlist)
    for artist in artists_in_a_playlist:
        print (artist)
        print("Länk till iframe: " + player)

    return render_template("result.html", artists_in_a_playlist = artists_in_a_playlist, name_of_playlist = name_of_playlist, player=player, city=city, weather_symbol=weather_symbol, temp=temp)

    if __name__ == "__name__":
        app.run(debug=True)
