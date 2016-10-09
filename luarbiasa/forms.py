from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import Item


class ItemForm(ModelForm):
	class Meta:
		model = Item
		exclude = ['id','image_url','user']
		widgets = {
				
		}

class LoginForm(forms.Form):
	username = forms.CharField(label='username', max_length=20)
	password = forms.CharField(label='password',max_length=20)

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets =  {

		}
		labels = {
			'username' : '',
			'password' : '',
		}
		help_texts = {
			'username' : '',
			'password' : '',
		}
		error_messages = {
            'NON_FIELD_ERRORS': {
                'password': '',
            }
		}