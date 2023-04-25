import requests

url_template_1 = 'https://wttr.in/Череповец?nTqM&lang=ru'
url_template_2 = 'https://wttr.in/Лондон?nTqM&lang=ru'
url_template_3 = 'https://wttr.in/Шереметьево?nTqM&lang=ru'
response = requests.get(url_template_1)
print(response.text)
response = requests.get(url_template_2)
print(response.text)
response = requests.get(url_template_3)
print(response.text) 	

