# Importerar funtionen som använder Google Maps Geocoding API
from geocoding_api import get_coordinates
# Importerar funktionen som använder SMHI's API
from smhi_api import get_weather_forecast
# Importerar funktionen som använder Spotify's API
from spotify_api import get_spotify_info
# Importerar funktionen som hämtar vädersymbolerna från smhi
from weather import get_weather_picture
from flask import Flask, request, render_template, jsonify
from flask import *

app = Flask(__name__)
prefix = '/api/v1'


@app.route(prefix + '/info_about/<city>', methods=['GET'])
def zephyr_api(city):
    coordinates = get_coordinates(city)
    weather_forecast = get_weather_forecast(coordinates[1], coordinates[0])
    spotify_data = get_spotify_info(weather_forecast['weather_symbol'])
 
    info = {
            'city': city,
            'cooordinates': {
                'latitude': coordinates[0],
                'longitude': coordinates[1]
            },
            'weatherInfo': {
                'temperature': weather_forecast['temperature'],
                'weatherSymbol': weather_forecast['weather_symbol']
            },
            'spotify': {
                'mood': spotify_data[2],
                'playlist': spotify_data[0],
                'spotifyLink': spotify_data[1]
            }
            }

    return jsonify(info)


@app.route('/')
def start():
    #visar startsidan där stad väljs, skickas vidare till route result
    return render_template("index.html")


@app.route('/about')
def info():
    #visar infosida om oss skapare
    return render_template("about.html")


@app.route('/result/', methods=['GET','POST'])
def find_city():
    # hämtar vilken stad som har angivits i formuläret
    city = request.form.get("city").title()
    # get_coordinates anropas med staden som argument för att ta fram koordinater
    # En lista innehållandes longitude och latitude returneras
    coordinates = get_coordinates(city)
    # get_weather_forecast anropas med koordinaterna som argument
    # En lista innehållandes temperatur och nuvarande vädersymbol returneras
    weather_forecast = get_weather_forecast(coordinates[1], coordinates[0])
    #tar ut endast vädersymbolen från weather_forecast.
    #SKa skickas till spotify och returneras i html result.
    weather_symbol = (weather_forecast['weather_symbol'])
    #tar ut endast temperaturen från weather_forecast
    #ska returneras till html result
    temp = (weather_forecast['temperature'])

    #hämtar ut bilden för vädersymbolen
    picture = get_weather_picture(weather_symbol)

    #get_spotify_info returnerar lista namnet på spellistan och länken till seplaren
    spotify_data = get_spotify_info(weather_symbol)
    name_of_playlist = spotify_data[0]
    link = spotify_data[1]

    return render_template("result.html", city=city, weather_symbol=weather_symbol, temp=temp, picture=picture, name_of_playlist=name_of_playlist, link=link )


if __name__ == "__name__":
    app.run(debug=True)
