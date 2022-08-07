from django.shortcuts import render

# Create your views here.
from .forms import * 
from .app import *

def wheather(request):
    main=''
    desc=''
    felltemp=''
    temp_min=''
    temp_max=''
    pressure=''
    humidity=''

    form=CityName(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            new_city = request.POST.get('textfield')
            print('hello',new_city)
            x=recursive_items(weather_fetch(new_city))
            try:
                for key,value in x:
                    if(key=='weather'):
                        dic=value[0]
                        main = dic['main']
                        desc=dic['description']
                    elif(key=='feels_like'):
                        felltemp=value
                    elif(key=='temp_min'):
                        temp_min=value
                    elif(key=='temp_max'):
                        temp_max=value
                    elif(key=='pressure'):
                        pressure=value
                    elif(key=='humidity'):
                        humidity=value
            except:
                pass
            
    return render(request,'wheather.html' , {'main ':main ,'desc':desc,'felltemp':felltemp,'temp_min':temp_min,'temp_max':temp_max,'pressure':pressure,'humidity':humidity})


