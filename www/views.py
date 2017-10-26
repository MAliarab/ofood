# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm

from .models import Customer
# Create your views here.

def homePage(request):

    html = '<p> you registered successfully</p> <p>Thanks for your registration :)</p>'

    return HttpResponse(html)

def signup(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)

        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        if Customer.objects.filter(phone=phone):

            form.add_error('phone' , 'phone number already exists')
        else:

            Customer.objects.create(name= name , phone=phone , email=email , password=password)

            return redirect('/home/')

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})