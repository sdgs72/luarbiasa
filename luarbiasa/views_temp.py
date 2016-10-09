#-------- DJANGO LIBRARY---------------#
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect


#-------------THIRD PARTY LIBRARY--------#
import requests
import cloudinary
import cloudinary.uploader
import cloudinary.api
import pprint
import json

#--------------CUSTOM LIBRARY-----------#
from .forms import ItemForm,UserForm,LoginForm
from .models import Item


# Create your views here.
def index(request):
	context = {}
	return render(request,'index.html',context);

def myAdmin(request):
	form_1 = ItemForm(request.POST or None)
	message = ""
	if form_1.is_valid():
		if request.FILES:
			message = "upload ok"
			image_file = request.FILES["fileToUploadname"]
			cloudinary.config( 
			  cloud_name = "dqvh7ldlu", 
			  api_key = "774866733655544", 
			  api_secret = "3w2pVmUzXHKVIh-ZYBhOTYKlsbA" 
			)
			item_object = form_1.save(commit=False)
			item_object.image_url = "http://res.cloudinary.com/dqvh7ldlu/image/upload/v1467507896/dunfw6sxlxhigiwgl1zc.jpg"
			item_object.save()
			#item_1 = Item()
			#print "HaSH RESULT"
			#print cloudinary.uploader.upload(image_file)
	context = {"form_1":form_1}
	return render(request,'myAdmin.html',context);




def search_result(request):
	location = request.GET['location']
	empty = ""
	brand_list = Item.objects.filter(location=location)
	if not brand_list:
		empty = "empty"
	context = {'location':location,"brand_list":brand_list,"empty":empty}
	return render(request,'search_result.html',context)

def user_admin(request):
	return render(request,'user_admin.html',{})

#This Function is used to serve the login page of our browser
def login_view(request):
	user_form = LoginForm(request.POST or None)
	error_message=""
	if user_form.is_valid():
		try:
			user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
			if user is not None:
				error_message = "success"
				login(request,user)
				return redirect('../myadmin')
			else:
				error_message = "user is none"
		except Exception as e:
				error_message = str(e)
		finally:
			if user is not None:
				return redirect('../myadmin')
			else:
				context = {"user_form":user_form,"error_message":error_message}
				return render(request,'login.html',context)
	else:
		context = {"user_form":user_form,"error_message":error_message}
		return render(request,'login.html',context)



def register(request):
	user_form = UserForm(request.POST or None)
	error_message=""
	if user_form.is_valid():
		try:
			user_instance = user_form.save() 
		except Exception as e:
			error_message = str(e)
		finally:
			context = {"user_form":user_form,"error_message":error_message}
			return render(request,'register.html',context)
	else:
		context = {"user_form":user_form,"error_message":error_message}
		return render(request,'register.html',context)



def logout_view(request):
	logout(request)	
	redirect('../login')


#-----------------------------------------AJAX CALLS------------------------------#


####ajax###
def getBannersByLocation(request):
	context = {}
	location = request.POST['location']
	result_list = Item.objects.filter(location=location).values()
	myArr = []
	for elem in result_list:
		print elem
		myArr.append(elem)
	print myArr
	return JsonResponse({"banner_list":myArr},safe=False)

def getBannersByLocationCreditCard(request):
	context = {}
	print request.POST
	location = request.POST['location']
	credit_card = request.POST['credit_card']
	print credit_card
	location = "jakarta"
	credit_card = ["BCA","CITIBANK"]
	print credit_card
	Q1 = Q(location=location)
	for elem in credit_card:
		Q1 = Q1 | Q(creditcard=elem)
	result_list = Item.objects.filter(Q1).values()
	myArr = []
	for elem in result_list:
		myArr.append(elem)
	return JsonResponse({"banner_list":myArr},safe=False)



