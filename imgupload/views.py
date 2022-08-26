from contextlib import redirect_stderr
from xml.dom.minidom import NamedNodeMap
from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import ImageUploadForm
from .test01 import *
from django.contrib import messages
from .connection import *
import datetime

# Create your views here.
def imgupload(request):
    return render(request,'plant.html')

def result(request):
    return render(request,'index.html')

def imageprocess(request): 
    form=ImageUploadForm(request.POST, request.FILES )
    if form.is_valid():
        handel_uploaded_file(request.FILES['image'])
        img_path = 'img.jpg'
        x=identify_plant(["img.jpg"])
        res_orginal=[]
        res_value=[]
        
        plant_name=''
        pclass = ''
        family=''
        genus=''
        kindom=''
        order=''
        phylum=''
        org_url=''

        similar_images=[]
        common_names=[]
        wiki_url=[]
        dis_desc=[]
        name=[]
        probability=[]

        

        for key,value in recursive_items(x):
            if(key=='suggestions'):
                for x1 in value:
                    for y,z in recursive_items(x1):


                        if(y=='common_names'):
                            #print(z)
                            res_orginal.append(z)
                        if(y=='value'):
                            #print(z)
                            res_value.append(z)
                        if(y=='plant_name'):
                            #print(z)
                            plant_name=z 
                        if(y=='class'):
                            #print(z)
                            pclass=z                        
                        if(y=='family'):
                            #print(z)
                            family=z
                        if(y=='genus'):
                            #print(z)
                            genus=z
                        if(y=='kingdom'):
                            #print(z)
                            kingdom=z
                        if(y=='order'):
                            #print(z)
                            order=z
                        if(y=='phylum'):
                            #print(z)
                            phylum=z
                        if(y=='url'):
                            #print(z)
                            org_url=z       
                        
            if(key=='diseases'):
                for x1 in value:
                    for y,z in recursive_items(x1):
                        if(y=='probability'):
                            probability.append(z)
                        if(y=='common_names'):
                            #print(z)
                            common_names.append(z)
                        if(y=='name'):
                            #print(z)
                            name.append(z)
                        if(y=='description'):
                            #print(z)
                            dis_desc.append(z)
                        if(y=='url'):
                            #print(z)
                            wiki_url.append(z)
                        if(y=='similar_images'):
                            #print(z)
                            a=z[0]
                            similar_images.append(a['url'])

        if(probability[0]<0.6):
            messages.error(request, 'Our Database not found very good match for this ')
            return redirect(imgupload)
            

        t=tables()
        for x in range(3):
            con=sql_connection()
            mycursor = con.cursor()
            querry="insert into plant values(%s,%s,%s,%s,now())"
            
            data=[str(plant_name),str(name[x]),probability[x],'bengluru']
            mycursor.execute(querry,data)
            mycursor.close()
            con.commit()

        return render(request,'result.html' , {'res_orginal':res_orginal,'res_value':res_value[0],'img_url':res_value[1],'pclass':pclass,'family':family,'genus':genus,'kindom':kindom,'order':order,'phylum':phylum,'org_url':org_url,'plant_name':plant_name,
        
        'common_names':common_names,'dis_desc':dis_desc,'wiki_url':wiki_url,'similar_images':similar_images,'name':name,'probability':probability})

def handel_uploaded_file(f):
    with open('img.jpg','wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def report(request):
    con=sql_connection()
    mycursor = con.cursor()
    querry="select d1,count(d1),round(avg(percentage)*100,2) from plant where uploaddate BETWEEN (NOW() - INTERVAL 7 DAY) AND NOW() group by d1 order by 2 desc;"
    mycursor.execute(querry)
    myresult=mycursor.fetchall()
    name=[]
    frequency=[]
    percentage=[]
    
    for x in myresult:
        # print(x[0],x[1])
        name.append(x[0])
        frequency.append(x[1])
        percentage.append(x[2])
    zipped=zip(name,frequency,percentage)
    return render(request,"report.html",{'zipped':zipped})
