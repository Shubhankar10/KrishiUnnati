'''import urllib, json
import urllib.request
from geopy.geocoders import Nominatim


apikey="6350f4054e660ee8b2e95d58c038accb"




           
city=str(input("Enter City Name"))            
geolocator = Nominatim(user_agent="MyApp")
location = geolocator.geocode(city)
x=location.latitude
y=location.longitude


forecast_url ="https://api.agromonitoring.com/agro/1.0/weather/forecast?lat=%s&lon=%s9&appid=%s"%(x,y,apikey)
current_url="https://api.agromonitoring.com/agro/1.0/weather?lat=%s&lon=%s9&appid=%s"%(x,y,apikey)

response_current = urllib.request.urlopen(current_url)
Json_Data_current = json.loads(response_current.read())


response_forecast = urllib.request.urlopen(forecast_url)
Json_Data_forecast = json.loads(response_forecast.read())
print(Json_Data_current)

for x in Json_Data_current:
    for key,value in recursive_items(x):
        print(key,value)

for x in Json_Data_forecast:
    for key,value in recursive_items(x):
        print(key,value)

'''

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)
