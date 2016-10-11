#-------- DJANGO LIBRARY---------------#
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect
from .models import Deal,Retailer
import pprint



def index(request):
	context = {}
	return render(request,'index.html',context);

def getDealsByLocation(request):
	context = {}
	myArr = []
#   location = request.GET['location']
	location = "MALL_KELAPA_GADING"
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



'''
{
	'Retailer ID' : {

	}		
	


}
'''
