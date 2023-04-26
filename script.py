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

for response in city:
	response = requests.get('https://wttr.in/', params=payload)
	response.raise_for_status()
	print(response.text)
