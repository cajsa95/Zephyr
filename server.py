# Importerar funtionen som använder Google Maps Geocoding API
from geocoding_api import get_coordinates
# Importerar funktionen som använder SMHI's API
from smhi_api import get_weather_forecast

def start():
	# Användaren skriver in en stad
	city = input('Välj stad: ')
	# get_coordinates anropas med staden som argument för att ta fram koordinater
	# En lista innehållandes longitude och latitude returneras
	coordinates_list = get_coordinates(city)

	''' TA BORT DETTA SEN '''
	print('*** ' + city.upper() + ' ***')
	print('*'*15)
	print('Longitude: ' + coordinates_list[0] + ' Latitude: ' + coordinates_list[1])

	# get_coordinates anropas med koordinaterna som argument
	# En lista innehållandes temperatur och nuvarande vädersymbol returneras
	weather_forecast = get_weather_forecast(coordinates_list[0], coordinates_list[1])
	
	''' TA BORT DETTA SEN '''
	print(weather_forecast)
	for i in weather_forecast:
		print(i)
	
def hej_spotify_vill_du_bestämma_symbol_tack_på_förhand(valfritt):
	pass

start()