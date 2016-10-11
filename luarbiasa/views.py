#-------- DJANGO LIBRARY---------------#
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect
from .models import Deal,Retailer,constants
import pprint, json

def index(request):
	location_choices_obj = constants.LOCATION_CHOICES
	location_choices = {}
	for location in constants.LOCATION_CHOICES:
		location_choices[location[1]] = location[0]
	print location_choices
	context = {"location_choices_obj": constants.LOCATION_CHOICES, "location_choices_str": json.dumps(location_choices)}
	return render(request,'index.html',context);

def getDealsByLocation(request):
	context = {}
	myArr = []
	print request.GET['location']
   	location = request.GET['location']
	# location = "MALL_KELAPA_GADING"
	retailer_list = Retailer.objects.filter(location=location).values()
	q1 = Q()
	for elem_retailer in retailer_list:
		deal_items = Deal.objects.filter(retailer_id=elem_retailer['id']).values()
		tempArr = []
		for deal in deal_items:
			deal['retailer_name'] = elem_retailer['brand_name']
			tempArr.append(deal)
		elem_retailer['deals'] = tempArr
		myArr.append(elem_retailer)
	return JsonResponse({"deals":myArr},safe=False)

def getAllLocations(request):
	return JsonResponse({"locations": constants.LOCATION_CHOICES})
