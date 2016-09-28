#-------- DJANGO LIBRARY---------------#
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.shortcuts import redirect


def index(request):
	context = {}
	return render(request,'live.html',context);
	

def live(request):
	context = {}
	return render(request,'live.html',context);
