import requests

url = ['https://wttr.in/Череповец', 'https://wttr.in/Лондон', 'https://wttr.in/Шереметьево']
payload = {'key': 'nTqM&lang=ru'}
i = 0

for response in url:
	url_patterns = url[i]
	response = requests.get(url_patterns, params=payload)
	response.status_code

	i += 1
	
	print(response.text)


