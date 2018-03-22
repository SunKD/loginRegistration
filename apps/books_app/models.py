# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..belt_reviewer_app.models import User

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return 'name {}'.format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books_written")
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()
    def __str__(self):
        return 'title: {}'.format(self.title)

class Review(models.Model):
    reviewer = models.ForeignKey(User, related_name="user_reviews")
    reviewed_book = models.ForeignKey(Book, related_name="book_reviews")
    comment = models.CharField(max_length=255)
    rating = models.IntegerField()
    def __str__(self):
		return 'reviewed_user {}, reviewed_book {}, comment {}, rating{}'.format(self.reviewer, self.reviewed_book, self.comment, self.rating)

