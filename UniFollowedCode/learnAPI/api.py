import requests

response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
content = response.json()
insult = content['insult']


url = f'https://www.purgomalum.com/service/json?text={insult}&fill_char=-'
response = requests.get(url)
data = response.json()
clean_insult = data['result']
print(clean_insult)
