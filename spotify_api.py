from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests

#Autentisering sker via Client Credentials flow dvs:
#client_id och client_secret är specifikt för just Zephyr
client_id='c7c574d9d26b448789d562cc1af24406'
client_secret='4082946357c043c2b959cfb557337f27'

#nödvändiga parametrar till API-anropet
grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

#URLn anropet till APIt utgår ifrån
url='https://accounts.spotify.com/api/token'

def get_spotify_info(weather_symbol):
    #Vädersymbolen från smhi's API avgör vilket "mood" det är på
    #listan som rekommenderas från Spotify,
    if weather_symbol == 1: #Clear Sky
        mood = 'happy'
    elif weather_symbol == 2: #Nearly Clear Sky
        mood = 'great day'
    elif weather_symbol == 3: #Variable cloudiness
        mood = 'sunshine'
    elif weather_symbol == 4: #Halfclear sky
        mood = 'calm'
    elif weather_symbol == 5: #Cloudy sky
        mood = 'sad'
    elif weather_symbol == 6: #Overcast
        mood = 'fuzzy'
    elif weather_symbol == 7: #Fog
        mood = "alone"
    elif weather_symbol == 8: #Rain showers
        mood = 'shower'
    elif weather_symbol == 9: #Thunderstorm
        mood = 'dark'
    elif weather_symbol == 10: #Light sleet
        mood = 'chill'
    elif weather_symbol == 11: #Snow showers
        mood = 'autumn'
    elif weather_symbol == 12: #Rain
        mood = 'rain'
    elif weather_symbol == 13: #Thunder
        mood = 'thunder'
    elif weather_symbol == 14: #Sleet
        mood = 'storm'
    elif weather_symbol == 15: #Snowfall
        mood = 'winter'
    else:
        return False

    #Skapa en accsess-token som är nödvändig för att komma åt APIt
    t = requests.post(url, data=body_params, auth = (client_id, client_secret))
    token = t.json()['access_token']

    #Anropet till spotifys API, spotify väljer själv ut 1 spellista beroende på vilket mood som skickas med
    r = requests.get("https://api.spotify.com/v1/search/?q=" + mood + "&type=playlist&limit=1", headers={"Authorization": "Bearer " + token})
    #SKA TA BORT DENNA RAD SEDAN print(r.json()['playlists']['items']['name'])
    data = (r.json())
    #SKA A BORT DENNA RAD SEDAN
    print("spotify")
    print(len(data))
    if len(data) == 0:
        return False
    else:

        #Loopar igenom resultatet och plockar ur spellistans namn och url
        for item in (data["playlists"]['items']):
            playlist = (item["name"])
            link = (item['uri'])

            #Skapar en tom lista och adderar in spellistans namn och url
            spotify_data = []
            spotify_data.append(playlist)
            spotify_data.append(link)
            spotify_data.append(mood)

            return spotify_data
