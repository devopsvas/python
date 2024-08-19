import requests 

respone = requests.get('http://api.open-notify.org/astros.json')
json = respone.json()
print(json)

for person in json['people']:
    print(person['name'])
    