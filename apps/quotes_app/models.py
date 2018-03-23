# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users_app.models import User

# Create your models here.
class AddManager(models.Manager):
    def addquote_validator(self, postData):
        result={
            'status': False
        }
        errors=[]
        if postData['quoter'] == "" or postData['quoter'] < 3 :
            errors.append("Quoted by should be more than 3 characters")
        
        if postData['message'] < 10:
            errors.append("message should be longer than 10 characters!")

        if len(errors):
            result['errors'] = errors
        else:
            result['status'] = True
        return result

class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.TextField(null=False, max_length=1000)
    uploader = models.ForeignKey(User, related_name="user_uploaded")
    favorite_users = models.ManyToManyField(User, related_name="favorite_quote")
    objects = AddManager()

    def __str__(self):
        return 'quoted_by {}, message {}, uploader {}, favorite_users{}'.format(self.quoted_by, self.message, self.uploader, self.favorite_users)


