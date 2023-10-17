import requests
import json
from keys import API_KEY
city = input("Enter the Name of the city\n")

url = f"{API_KEY}={city}"

r = requests.get(url)

wdic = json.loads(r.text)
print(f"The temperature of {city} in Celsius is {wdic['current']['temp_c']}")
print(f"The temperature of {city} in Fahrenheit is {wdic['current']['temp_f']}\n\n")

print(f"The Speed of Wind in {city} is {wdic['current']['wind_kph']} KPH")
print(f"The Speed of Wind in {city} is {wdic['current']['wind_mph']} MPH\n\n")

for key,value in wdic['location'].items():
    print(f"{key} --> {value}")