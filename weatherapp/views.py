from django.shortcuts import render
import urllib, json
import urllib.request
from geopy.geocoders import Nominatim
from .weather import *

import datetime
from rfc3339 import rfc3339

# Create your views here.

apikey="6350f4054e660ee8b2e95d58c038accb"

def input(request):
    return render(request,'weather.html')

def result(request):
    city=str(request.POST.get('Cityname'))           
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    print(type(location))
    x=location.latitude
    y=location.longitude
    
    forecast_url ="https://api.agromonitoring.com/agro/1.0/weather/forecast?lat=%s&lon=%s9&appid=%s"%(x,y,apikey)
    response_forecast = urllib.request.urlopen(forecast_url)
    Json_Data_forecast = json.loads(response_forecast.read())
    responsedate=[]
    responsedescription=[]
    responsetemp=[]
    responsehumidity=[]
    


    for x in Json_Data_forecast:
        for key,value in recursive_items(x):
            if(key=='dt'):
                date=int(value)
                date_json=date*1000
                dt= datetime.datetime.fromtimestamp(date_json / 1000.0, tz=datetime.timezone.utc)
                date_csv = rfc3339(dt, utc=True, use_system_timezone=False)
                date_final=date_csv[0:16].replace("T"," ")
                responsedate.append(date_final)
            if (key=='weather'):
                description=value[0]['description']
                responsedescription.append(description)
            if (key=='temp'):
                temp=value-273
                responsetemp.append(temp)

            if (key=='humidity'):
                responsehumidity.append(value)
                             
    zipped=zip(responsedate,responsedescription,responsetemp,responsehumidity)
    


           


            

    
    
    return render(request,'wresult.html',{'location':location.address,'responsedate':responsedate,'responsedescription':responsedescription,'responsetemp':responsetemp,'zipped':zipped})