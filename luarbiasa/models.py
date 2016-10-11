from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from .constants.py import 
# Create your models here.

class constants():	
	CC_CHOICES = (
		('BNI','BNI'),
		('BCA','BCA'),
		('MANDIRI','MANDIRI'),
		('MEGA','MEGA'),
		('NONE','NONE'),
	)
	CATEGORY_CHOICES = (
		('FASHION','FASHION'),
		('ELECTRONIC','ELECTRONIC'),
		('FOOD_AND_BEVERAGE','Food and Beverage'),
	)
	LOCATION_CHOICES = (
		('MALL_KELAPA_GADING','Mall Kelapa Gading'),
		('GRAND_INDONESIA','Grand Indonesia'),
		('PONDOK_INDAH_MALL_1','Pondok Indah Mall 1'),
		('PONDOK_INDAH_MALL_2','Pondok Indah Mall 2'),
		('PONDOK_INDAH_MALL_3','Pondok Indah Mall 3'),	
	)

class Deal(models.Model):
	id = models.AutoField(primary_key=True)		#indexing is enabled automatically for primary key
	retailer_id = models.ForeignKey('Retailer',blank=True) #indexing is enabled automatically for foreign key
	credit_card = models.CharField(choices=constants.CC_CHOICES,max_length=20,blank=True,default='NONE')
	start_date = models.DateTimeField(blank=True)
	end_date = models.DateTimeField(blank=True)
	#is_active = models.CharField(max_length=200,blank=True) 
	summary = models.CharField(max_length=256,blank=True)
	description = models.CharField(max_length=2000,blank=True)
	picture_link = models.CharField(max_length=512,blank=True)
	def __str__(self):
		return '%s : %s : %s' % (self.retailer_id.brand_name, self.credit_card, self.summary)

class Retailer(models.Model):
	id = models.AutoField(primary_key=True)					  #indexing is enabled automatically for primary key 
	brand_name = models.CharField(max_length=256,blank=True)
	category = models.CharField(choices=constants.CATEGORY_CHOICES,max_length=256,blank=True)
	description = models.CharField(max_length=2000,blank=True)
	location = models.CharField(max_length=256,choices=constants.LOCATION_CHOICES,blank=True)
	address = models.CharField(max_length=256,blank=True)	
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	picture_link = models.CharField(max_length=512,blank=True)
	def __str__(self):	
		return self.brand_name
	#deals_id = models.CharField(max_length=200,blank=True)



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