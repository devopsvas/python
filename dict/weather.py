import requests

city = input('Please input city name\n')

url = 'http://api.weatherapi.com/v1/current.json?key=454cca8c51b64130b0d130029240706 &q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

#print(weather_json)


temp = weather_json.get('current').get('temp_c')
condi = weather_json.get('current').get('condition').get('text')

#print(temp)
#print(condi)

print("Today's weather in", city,  'is', condi, 'and', temp, 'degrees')
