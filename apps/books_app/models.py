# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..belt_reviewer_app.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()
    def __str__(self):
        return 'title: {}'.format(self.title)

class Review(models.Model):
    reviewed_user = models.ForeignKey(User, related_name="reviewed_book")
    reviewed_book = models.ForeignKey(Book, related_name="reviewer")
    rating = models.IntegerField()
    def __str__(self):
		return 'reviewed_user {}, reviewed_book {}, rating{}'.format(self.reviewed_user, self.reviewed_book, self.rating)

class Author(models.Model):
	name = models.CharField(max_length=255)
	wrote_book = models.ForeignKey(Book, related_name="writer")
	def __str__(self):
		return 'name {}, wrote_book {}'.format(self.name, self.wrote_book)