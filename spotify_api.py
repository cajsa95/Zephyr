from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import requests

#Hämtar information från Spotify. Autentisering via Client Credentials flow dvs:
#client_id och client_secret är specifikt för Zephyr
client_credentials_manager = SpotifyClientCredentials(client_id='c7c574d9d26b448789d562cc1af24406', client_secret='4082946357c043c2b959cfb557337f27')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Symbolen som avgör vilken spellista som ska rekomenderas, finns 1-15 st hämtade från SMHIs API
weather_symbol = "12"

if weather_symbol == "1": #Clear Sky
    song_id = "37i9dQZF1DXdPec7aLTmlC" #Happy hits!
elif weather_symbol == "2": #Nearly Clear Sky
    song_id = "37i9dQZF1DX1y2vWSgwjbV" #Life is good!
elif weather_symbol == "3": #Variable cloudiness
    song_id = "37i9dQZF1DXcwkNsfYPDPQ" #Feeling good låtar!
elif weather_symbol == "4": #Halfclear sky
    song_id = "37i9dQZF1DWU0ScTcjJBdj" #Relax & Unwind
elif weather_symbol == "5": #Cloudy sky
    song_id = "37i9dQZF1DX1qJrMsOBLRT" #När löven faller
elif weather_symbol == "6": #Overcast
    song_id = "37i9dQZF1DX1s9knjP51Oa" #Calm Vibes
elif weather_symbol == "7": #Fog
    song_id = "37i9dQZF1DWWuOw4E4LGde" #Stillsamt mörker
elif weather_symbol == "8": #Rain showers
    song_id = "37i9dQZF1DWVYh7Tdj3ZL8" #En regning dag
elif weather_symbol == "9": #Thunderstorm
    song_id = "37i9dQZF1DWSlw12ofHcMM" #Swagger
elif weather_symbol == "10": #Light sleet
    song_id = "37i9dQZF1DWSqBruwoIXkA" #Down in the dumps
elif weather_symbol == "11": #Snow showers
    song_id = "37i9dQZF1DXbi6K7zACoDU" #Vintermys
elif weather_symbol == "12": #Rain
    song_id = "37i9dQZF1DXbvABJXBIyiY" #Rainy day
elif weather_symbol == "13": #Thunder
    song_id = "37i9dQZF1DX2pSTOxoPbx9" #Dark & Stormy
elif weather_symbol == "14": #Sleet
    song_id = "37i9dQZF1DX3YSRoSdA634" #Life sucks
elif weather_symbol == "15": #Snowfall
    song_id = "37i9dQZF1DWTEpIN9mg9FS" #Winter chills
else:
    print("Something went terrible wrong, sorry!")


#Skapar det representerar en spellista i Spotifys API
uri = ('spotify:user:spotify:playlist:' + song_id)
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

#Resulatet från APIt innehållandes all information om listan, kommer ut i json
results = sp.user_playlist(username, playlist_id)

jsonData = json.dumps(results)
data = json.loads(jsonData)

#Skapar en tom lista
artist_list = []

#För varje sak i json-datan ska vi ta ut namnet på artisten och lägga till i artist_list
for item in (data["tracks"]["items"]):
    for i, y in enumerate(item["track"]["artists"]):
        #print(y["name"])
        all_artists = (y["name"])
        artist_list.append(all_artists)


#För att enbart printa ut alla artister i terminalen
#for artist in list(set(artist_list)):
    #print(artist)

#För att undvika dubletter i artist_list, finns en artist redan i listan så skrivs artisten bara ut en gång
artists_in_a_playlist = (list(set(artist_list)))
#Får ut namnet på spellistan
name_of_playlist = (data["name"])
#Skapar länken till spotifys online player
player = ("https://open.spotify.com/embed/user/spotify/playlist/" + song_id)

return artists_in_a_playlist, name_of_playlist, player
