# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'users_app/index.html')

def register(request):
    response = User.objects.register_validator(request.POST)
    if response['status'] == True:
        request.session['user_id'] = response['user_id']
        return redirect(reverse('quote_index'))
    else: 
        for error in response['errors']:
            messages.error(request, error)
        return redirect(reverse('user_index'))

    return redirect(reverse('quote_index'))

def login(request):
    response = User.objects.login_validator(request.POST)
    if response['status'] == True:
        request.session['user_id'] = response['user_id']
        return redirect(reverse('quote_index'))
    else: 
        for error in response['errors']:
            messages.error(request, error)
        return redirect(reverse('user_index'))

    return redirect(reverse('quote_index'))