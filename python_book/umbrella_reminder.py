import sys, requests

if len(sys.argv) < 2:
    print("Błąd: Podaj klucz API!")
else:
    api_key = sys.argv[1]
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid={api_key}"
    response = requests.get(url)
    dane_pogody = response.json()
    
    dane = dane_pogody['weather'][0]['main']

    if dane in ['Rain', 'Drizzle', 'Thunderstorm']:
        print("Pamiętaj o zabraniu parasola!")
    else:
        print("Nie musisz brać parasola.")
    print(f"Obecna pogoda: {dane}")