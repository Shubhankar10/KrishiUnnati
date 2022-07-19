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
        res_dis=[]
        res_desc=[]
        res_local=[]
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
            if(key=='diseases'):
                for x1 in value:
                    for y,z in recursive_items(x1):
                        if(y=='common_names'):
                            #print(z)
                            res_dis.append(z)
                        if(y=='description'):
                            #print(z)
                            res_desc.append(z)
                        if(y=='local_name'):
                            #print(z)
                            res_local.append(z)


        return render(request,'result.html' , {'res_orginal':res_orginal,'res_value':res_value,'res_dis':res_dis,'res_desc':res_desc,'res_local':res_local})

def handel_uploaded_file(f):
    with open('img.jpg','wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)