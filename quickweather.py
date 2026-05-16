#! python3
# quickWeather.py - Prints the weather for a location from the command line.


import json, requests, sys

# Compute location from command line arguments.
APPID = '11e7033952c3668a3bf931e30549dc72'


if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
location = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={APPID}&units=metric"
#pobiera dane od strony
response = requests.get(url)
# i sprawdza czy dziala jesli nie to bedzie blad 401 
response.raise_for_status()

# .text to jest tekst ktory zwrocila nam strona
weatherData = json.loads(response.text)

w = weatherData["list"]

print(f"Pogoda dla: {location.title()}\n")

# w[0] to najbliższa prognoza (teraz/najbliższe 3h)
print("Dzisiaj (najbliższa prognoza):")
print(f"Zjawisko: {w[0]['weather'][0]['main']} - {w[0]['weather'][0]['description']}")
print(f"Temperatura: {w[0]['main']['temp']} °C\n")

# w[8] to prognoza za około 24 godziny (przeskok o 8 bloków po 3 godziny)
print("Jutro (o tej samej porze):")
#tutaj jest f string wiec jesli napisalismy weather to szuka elemntu weather i main 
print(f"Zjawisko: {w[8]['weather'][0]['main']} - {w[8]['weather'][0]['description']}")
print(f"Temperatura: {w[8]['main']['temp']} °C\n")

# w[16] to prognoza za około 48 godzin (przeskok o 16 bloków po 3 godziny)
print("Pojutrze (o tej samej porze):")
print(f"Zjawisko: {w[16]['weather'][0]['main']} - {w[16]['weather'][0]['description']}")
print(f"Temperatura: {w[16]['main']['temp']} °C")
