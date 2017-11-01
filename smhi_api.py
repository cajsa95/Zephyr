# Importerar modulen requests som behövs för förfrågningar över HTTP
import requests

def get_weather_forecast(longitude, latitude):
	try:
		# Gör en GET-förfrågan till APIet med koordinaterna Google Maps Geocoding API returnerade
		weather_forecast = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp2g/version/2/geotype/point/lon/' + longitude + '/lat/' + latitude + '/data.json')
		# Den returnerade JSON parsas
		results = weather_forecast.json()['timeSeries']

		# Gör en GET-förfrågan till APIet för att få ut alla giltiga tider för prognoser
		get_valid_times = requests.get("https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/validtime.json")
		# Väljer den aktuella tiden
		current_valid_time = get_valid_times.json()["validTime"][0]

		# Skapar ett tomt lexikon
		result_dict = {}

		# Loopar igenom den returnerade JSON
		for item in results:
			# Letar reda på aktuell prognos
			if item['validTime'] == current_valid_time:
				# Loopar igenom alla parametrar
				for parameter in item['parameters']:
					# Tar ut parametrar för temperatur och vädersymbol
					if parameter['name'] == 't':
						result_dict['temperature'] = parameter['values'][0]
					elif parameter['name'] == 'Wsymb':
						result_dict['weather_symbol'] = parameter['values'][0]
		# Returnerar lexikonet
		return result_dict

	except:
		print("smhi gick fel")
		return False
