from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
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