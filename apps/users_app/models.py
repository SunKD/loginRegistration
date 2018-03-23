# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        result ={
            'status' : False
        }
        
        errors = []
        print postData
        if postData['fullname'] == "":
            errors.append("Name should be more than 1 characters")
        if postData['alias'] == "":
            errors.append("Name should be more than 1 characters")
        if postData['email'] == "":
            errors.append("Email should be more than 5characters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email address is not valid")
        else:
            if len(User.objects.filter(email = postData['email'])) > 0:
                print User.objects.filter(email = postData['email'])
                errors.append("Email address already exists!")
        if postData['password'] == "":
            errors.append("Password should be more than 8characters")
        if not PASSWORD_REGEX.match(postData['password']):
            errors.append("Password should include contain one upper letter, one lowerletter and number ")
        if postData["password"] != postData["confirm_pw"]:
            errors.append("Passwords do not matched!")
        if postData["dob"] =="":
            errors.append("Birthday must be entered!")

        if len(errors):
            result['errors'] = errors
        else:
            new_user = User.objects.create(
                name = postData['fullname'],
                alias = postData['alias'],
                email = postData['email'],
                password = bcrypt.hashpw((postData['password']).encode(), bcrypt.gensalt()),
                dob = postData['dob']
            )      
            result['status'] = True
            result['user_id'] = new_user.id
        return result

    def login_validator(self, postData):
        result={
            'status': False
        }
        
        errors=[]
        existing = User.objects.filter(email = postData['loginemail'])
        if len(existing) < 1:
            errors.append("User name is not exist! Please register")
        else:
            password = existing[0].password
            if password != None:
                if bcrypt.checkpw(postData['loginpw'].encode(), password.encode()):
                    errors.append("Password is not matching")

            elif password == None:
                errors.append("user name is not matching")        
        
        if len(errors):
            result['errors'] = errors
        else:
            result['status'] = True
            result['user_id'] = existing[0].id
        return result


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.name, self.alias, self.email, self.dob)
    
