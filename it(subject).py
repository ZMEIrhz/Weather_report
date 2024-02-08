import pandas 
import requests 
import datetime 
while True:
    try:
        print('укажите город') 
        city = input()
        print('сколько дней(число 1-16)')
        cnt = (input())
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=771484946c02f120b4ff31b3e699e8d6'
        weather  = requests.get(url).json()
        dolgota = str(weather['coord']['lon'])
        shirota = str(weather['coord']['lat'])
        print(shirota, dolgota) 
        main_url = 'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=771484946c02f120b4ff31b3e699e8d6'
        weather = '' 
        weather = requests.get(main_url).json() 
        print(weather)
    except (KeyError): 
        print('нет такого города') 
        continue

    

 
 
 

 

