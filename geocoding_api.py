# Importerar modulen requests som behövs för förfrågningar över HTTP
import requests

def get_coordinates(city):
	# Grunden till URLen som används med APIet
	base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	# Zephyr's API-nyckel som krävs för att använda APIet
	api_key = 'AIzaSyBIdoaaYSWsSn4O8b4GoEU5tDzTG8gz_IU'
	# Fullständig URL, base_url + stad + API-nyckel
	url = (base_url + city + '&key=' + api_key)
	# Gör en GET-förfrågan till APIet
	request = requests.get(url)
	# Den returnerade JSON parsas
	results = request.json()['results']
	# Tar ut endast koordinaterna
	coordinates = results[0]['geometry']['location']

	# Koordinaterna måste göras om till strängar och får max ha 6st decimaler för att fungera med SMHI's API
	longitude = str(round(coordinates['lng'], 6))
	latitude = str(round(coordinates['lat'], 6))

	# Lägger koordinaterna i en lista
	coordinates_list = [longitude, latitude]

	# Returnerar listan
	return coordinates_list