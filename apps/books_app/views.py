# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'books_app/index.html')

def logout(request):
	request.session.clear()
	return redirect('/belt_reviewer_app/')