from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Restaurant
class SignUpForm(forms.Form):

    username = forms.CharField(max_length=50, help_text='you must enter maximum 50 characters')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=11 , min_length=11, help_text='Phone number must be in this form 09*********')
    password = forms.CharField(min_length=8 , show_hidden_initial='at least 8 characters')



class Search(forms.Form):

    choice = Restaurant.objects.all()
    restaurant = forms.ChoiceField(choices=choice)
