import requests

city = [
	'Череповец', 	
	'Лондон', 
	'Шереметьево'
]

payload = {
	'nTqM': '',
	'lang': 'ru',
}
	
for city_templates in city:
	response = requests.get(f'https://wttr.in/{city_templates}', params=payload)
	response.raise_for_status()
	print(response.text)