from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from .constants.py import 
# Create your models here.

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,blank=True,null=True)
    brand = models.CharField(max_length=200,blank=True)
    location = models.CharField(max_length=200,blank=True)
    image_url = models.CharField(max_length=200,blank=True)
    creditcard = models.CharField(max_length=200,blank=True)
    description = models.CharField(max_length=200,blank=True)
    timestamp_start = models.CharField(max_length=200,blank=True)



class Deals(models.Model):
	id = models.AutoField(primary_key=True)
	retailer_id = models.ForeignKey('Retailer')
	credit_card = models.CharField(max_length=200,blank=True)
	start_date = models.CharField(max_length=200,blank=True)
	end_date = models.CharField(max_length=200,blank=True)
	is_active = models.CharField(max_length=200,blank=True)
	summary = models.CharField(max_length=200,blank=True)
	description = models.CharField(max_length=2000,blank=True)
	picture_link = models.CharField(max_length=200,blank=True)

class Retailer(models.Model):
	id = models.AutoField(primary_key=True)
	brand_name = models.CharField(max_length=200,blank=True)
	category = models.CharField(max_length=200,blank=True)
	description = models.CharField(max_length=200,blank=True)
	location = models.CharField(max_length=200,blank=True)
	address = models.CharField(max_length=200,blank=True)
	Longitude = models.CharField(max_length=200,blank=True)
	latitude = models.CharField(max_length=200,blank=True)
	picture_link = models.CharField(max_length=200,blank=True)
	deals_id = models.CharField(max_length=200,blank=True)



'''
User
	unique id
	Username (email address)
	password
	User_type (group type)
	Super admin (django staff - default)
	Admin (wowdeals staff - non-mvp)
	Normal user (application user - mvp)
	Retailer staff (retailer user - mvp)
'''

'''
Deals
	Unique id
	Retailer id
	Credit card (filter - not mvp)
	Start date (timestamp)
	End date (timestamp)
	Is_active (optional; use end date instead)
	Summary (max 140chars : example-> beli 1 dapet 1)
	Description (max 2000chars : example-> syarat dan ketentuan)
	Picture link (optional, default to retailer logo)
'''

'''
Retailer
	Unique id
	Brand name
	Category
	Description
	Location (standardized mal-kelapa-gading) -> index + search query
	Address
	Longitude 
	Latitude
	Logo link
	Deals ID (array of ID) (limit to 20 all deals / retailer) (sort by enddate)
'''