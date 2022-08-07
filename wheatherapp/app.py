
import requests
from .config import * 

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    try:
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        return x
    except:
        pass 

    
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)

        else:
            yield (key, value)

'''
try:
    x=recursive_items(weather_fetch('Kotma'))
    for key,value in x:
        print(key,value)

except:
    pass

'''