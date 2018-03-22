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