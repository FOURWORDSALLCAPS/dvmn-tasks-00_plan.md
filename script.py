import requests

citys = [
	'Череповец', 	
	'Лондон', 
	'Шереметьево'
]

payload = {
	'nTqM': '',
	'lang': 'ru',
}
	
for city in citys:
	response = requests.get(f'https://wttr.in/{city}', params=payload)
	response.raise_for_status()
	print(response.text)
