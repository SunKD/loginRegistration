# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'belt_reviewer_app/index.html')

def register(request):
    response = User.objects.register_validator(request.POST)
    if response['status'] == True:
        request.session['user_id'] = response['user_id']
        return redirect('/books/')
    else: 
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/')

    return redirect('/books/')

    # errors = User.objects.basic_validator(request.POST)
    # if len(errors):
    #     for tag, error in errors.iteritems():
    #         messages.error(request, error, extra_tags = tag)
    #     return redirect('/')
    # else:
    #     fullname = request.POST['fullname']
    #     alias = request.POST['alias']
    #     email = request.POST['email']
    #     password = bcrypt.hashpw((request.POST['password']).encode(), bcrypt.gensalt())        
    #     user = User.objects.create(name=fullname, alias=alias, email=email, password=password)
    #     request.session['user_id'] = user.id
    #     return redirect('/books/')

def login(request):
    response = User.objects.login_validator(request.POST)
    if response['status'] == True:
        request.session['user_id'] = response['user_id']
        return redirect('/books/')
    else: 
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/')

    return redirect('/books/')