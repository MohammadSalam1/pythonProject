import requests

response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
content = response.json()
hello = content['insult']

print(hello)

import requests

response = requests.get('https://www.purgomalum.com/service/json?text=this is some test input')
content = response.json()
just = content['result']
print(just)

