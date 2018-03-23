# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..users_app.models import User
from models import *
from django.core.urlresolvers import reverse
from time import gmtime, strftime

# Create your views here.
def index(request):
	if 'user_id' not in request.session:
		return redirect(reverse('user_index'))
	else:
		user = User.objects.get(id = request.session['user_id'])
		all_users = User.objects.all()
		favorite = Quote.objects.filter(favorite_users =  request.session['user_id'])
		quotes = Quote.objects.all().exclude(favorite_users = user)
		print favorite
		context = {
			"user" : user,
			"all_user": all_users,
			"quotes": quotes,
			"favorites": favorite
		}
	return render(request, 'quotes_app/index.html', context)
	
def new(request):
	if 'user_id' not in request.session:
		return redirect(reverse('user_index'))
	quotes = Quote.objects.all()
	return render(request, 'quotes_app/index.html', {'quotes': quotes})

def add_quote(request):
	if 'user_id' not in request.session:
		return redirect(reverse('user_index'))

	response = Quote.objects.addquote_validator(request.POST)
	if response['status'] == True:
		user = User.objects.get(id = request.session['user_id'])
		new_quote = Quote.objects.create(
			quoted_by = request.POST['quoter'],
			message = request.POST['message'],
			uploader= user
		)
	else:
		for error in response['errors']:
			messages.error(request, error)

	return redirect(reverse('quote_index'))

def favorite(request):
	user = User.objects.get(id = request.session['user_id'])
	quote_id=request.POST['qid']
	quote = Quote.objects.get(id = quote_id)
	user.favorite_quote.add(quote)
	return redirect(reverse('quote_index'))

def remove_favorite(request):
	user = User.objects.get(id = request.session['user_id'])
	quote_id=request.POST['favoriteid']
	quote = Quote.objects.get(id = quote_id)
	user.favorite_quote.remove(quote)
	return redirect(reverse('quote_index'))

def view_user(request, id):
	user = User.objects.get(id= id)
	quotes = Quote.objects.filter(uploader_id = user.id)
	count = quotes.count()
	context ={
		'user' : user,
		'quotes' : quotes,
		'count' : count
	}
	return render(request, 'quotes_app/view_user.html', context)

def delete(request, id):
	if 'user_id' not in request.session:
		return redirect(reverse('user_index'))
	Review.objects.get(id = id).delete()
	return redirect(reverse('user_index'))


def logout(request):
	request.session.clear()
	return redirect(reverse('user_index'))