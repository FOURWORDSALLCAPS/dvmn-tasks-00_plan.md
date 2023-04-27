import requests

<<<<<<< HEAD
citys = [
=======
city = [
>>>>>>> b7eeaab40fddb58db1a8ff03796273db23b4cf62
	'Череповец', 	
	'Лондон', 
	'Шереметьево'
]

payload = {
	'nTqM': '',
	'lang': 'ru',
}
	
<<<<<<< HEAD
for city in citys:
	response = requests.get(f'https://wttr.in/{city}', params=payload)
=======
for city_templates in city:
	response = requests.get(f'https://wttr.in/{city_templates}', params=payload)
>>>>>>> b7eeaab40fddb58db1a8ff03796273db23b4cf62
	response.raise_for_status()
	print(response.text)