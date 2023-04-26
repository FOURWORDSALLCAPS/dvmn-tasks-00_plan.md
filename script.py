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
	print(response.text)
