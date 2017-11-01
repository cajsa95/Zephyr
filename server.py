# Importerar funtionen som använder Google Maps Geocoding API
from geocoding_api import get_coordinates
# Importerar funktionen som använder SMHI's API
from smhi_api import get_weather_forecast
# Importerar funktionen som använder Spotify's API
from spotify_api import get_spotify_info
# Importerar funktionen som hämtar vädersymbolerna från smhi
from weather import get_weather_picture
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
prefix = '/api/v1'


@app.route(prefix + '/info_about/<city>', methods=['GET'])
def zephyr_api(city):
    coordinates = get_coordinates(city)
    weather_forecast = get_weather_forecast(coordinates[1], coordinates[0])
    spotify_data = get_spotify_info(weather_forecast['weather_symbol'])

    info = {
            'city': city,
            'coordinates': {
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
    try:
        # hämtar vilken stad som har angivits i formuläret
        city = request.form.get("city").title()
        # get_coordinates anropas med staden som argument för att ta fram koordinater
        # En lista innehållandes longitude och latitude returneras
        coordinates = get_coordinates(city)
        if not coordinates:
            return render_template("false_city.html")
        else:
            # get_weather_forecast anropas med koordinaterna som argument
            # En lista innehållandes temperatur och nuvarande vädersymbol returneras
            weather_forecast = get_weather_forecast(coordinates[1], coordinates[0])
            if not weather_forecast:
                return render_template("not_in_range.html")
            else:
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
                if not spotify_data:
                    return render_template("spotify_fail.html")
                else:
                    name_of_playlist = spotify_data[0]
                    link = spotify_data[1]

                    return render_template("result.html", city=city, weather_symbol=weather_symbol, temp=temp, picture=picture, name_of_playlist=name_of_playlist, link=link )
    except:
        return render_template("page_not_found.html")


if __name__ == "__name__":
    app.run(debug=True)
