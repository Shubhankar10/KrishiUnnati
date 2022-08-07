from django.shortcuts import render
from .forms import ImageUploadForm
from .test01 import *


# Create your views here.
def imgupload(request):
    return render(request,'upload.html')

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



        return render(request,'result.html' , {'res_orginal':res_orginal,'res_value':res_value[0],'img_url':res_value[1],'pclass':pclass,'family':family,'genus':genus,'kindom':kindom,'order':order,'phylum':phylum,'org_url':org_url,'plant_name':plant_name,
        
        'common_names':common_names,'dis_desc':dis_desc,'wiki_url':wiki_url,'similar_images':similar_images,'name':name})

def handel_uploaded_file(f):
    with open('img.jpg','wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)