from django.shortcuts import render
from django.http import HttpResponse
from chatBackend.chat import  chat
from django.views.generic import TemplateView
# Create your views here.

class mainpage(TemplateView):
	Template_view="index.html"

	def get(self,request):
		return render(request,self.Template_view)

	def post(self,request):
		if request.method == 'POST':
			user = request.POST.get('input',False)
			context={"user":user,"bot":chat(request)}
			
		return render(request,self.Template_view,context)

def detail(request):
		return render(request,'details.html')

def login(request):
		return render(request,'login.html')

def signup(request):
		return render(request,'signup.html')

def map(request):
		return render(request,'map.html')
'''
def detail(request):
		return render(request,'details.html')
'''
