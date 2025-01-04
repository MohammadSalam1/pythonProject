import requests

response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
content = response.json()
hello = content['insult']

print(hello)

