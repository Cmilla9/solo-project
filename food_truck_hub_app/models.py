from django.db import models
import re
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First Name should be at least 3 letters long."
        if len(postData['last_name']) < 3:
            errors['first_name'] = "Last Name should be at least 3 letters long."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        if len(postData['password']) < 8:
            errors['password'] ='Password should be at least 8 characters or more.'
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = 'Passwords need to match.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BusinessUserManager(models.Manager):
    def business_validate(self, postData):
        errors = {}
        if len(postData['business_name']) < 3:
            errors['business_name'] = "Business Name should be at least 3 letters long."
        if len(postData['description']) < 5:
            errors['description'] = "Description should be 5 characters or more."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        if len(postData['password']) < 8:
            errors['password'] ='Password should be at least 8 characters or more.'
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = 'Passwords need to match.'
        return errors
    def business_update(self, postData):
        errors = {}
        if len(postData['business_name']) < 3:
            errors['business_name'] = "Business Name should be at least 3 letters long."
        if len(postData['description']) < 5:
            errors['description'] = "Description should be 5 characters or more."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        return errors

class BusinessUser(models.Model):
    business_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    food_category = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    password = models.CharField(max_length=25)
    current_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BusinessUserManager()