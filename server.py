# Importerar funtionen som använder Google Maps Geocoding API
from geocoding_api import get_coordinates
# Importerar funktionen som använder SMHI's API
from smhi_api import get_weather_forecast
# Importerar funktionen som använder Spotify's API
from spotify_api import get_spotify_info

def start():
    # Användaren skriver in en stad
    city = input('Välj stad: ')
    # get_coordinates anropas med staden som argument för att ta fram koordinater
    # En lista innehållandes longitude och latitude returneras
    coordinates_list = get_coordinates(city)

    #''' TA BORT DETTA SEN '''
    print('*** ' + city.upper() + ' ***')
    print('*'*15)
    print('Longitude: ' + coordinates_list[0] + ' Latitude: ' + coordinates_list[1])

    # get_coordinates anropas med koordinaterna som argument
    # En lista innehållandes temperatur och nuvarande vädersymbol returneras

    weather_forecast = get_weather_forecast(coordinates_list[0], coordinates_list[1])

    # SKRIVER BARA UT FÖR ATT SE ATT DICT ÄR RÄTT
    #print(weather_forecast)
    #''' TA BORT DETTA SEN '''
    #for i in weather_forecast:
        #print(i + ': ' + str(weather_forecast[i]))


    #DENNA SKA SKICKAS TILL SPOTIFY
    weather_symbol = (weather_forecast['weather_symbol'])
    #print(weather_symbol)

    spotify_data = get_spotify_info(weather_symbol)
    artists_in_a_playlist = spotify_data[0]
    name_of_playlist = spotify_data[1]
    player = spotify_data[2]

    print("We found this playlist for you: " + name_of_playlist)
    for artist in artists_in_a_playlist:
        print (artist)
    print("Länk till iframe: " + player)

start()
