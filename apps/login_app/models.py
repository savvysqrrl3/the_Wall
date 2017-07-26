from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
	def registerValidation(self, postData):
		results = {'status': True, 'errors': []}
		user = []
		if not postData ['firstnm'] or len(postData ['firstnm']) < 2:
			results['status'] = False
			results['errors'].append('First name must be at least 2 characters long.')
		if not postData ['lastnm'] or len(postData ['lastnm']) < 2:
			results['status'] = False
			results['errors'].append('Last name must be at least 2 characters long.')
		if not postData ['email'] or len(postData ['email']) < 4 or not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Email is not valid.')
		if not postData ['pw'] or len(postData ['pw']) < 5 or postData['pw'] != postData['confirmpw']:
			results['status'] = False
			results['errors'].append('Please confirm password is at least 5 characters long and matches your confirmation.')
		if results['status'] == True:
			user = User.objects.filter(email = postData['email'])
		if len(user) != 0:
			results['status'] = False
			results['errors'].append('Email already exists. Please try another email, or Log In.')
		return results

	def loginValidation(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['email']) < 3:
			results['status'] = False
			results['errors'].append('Something went wrong! Please try again.')
		else:
			user = User.objects.filter(email = postData['email'])
			if len(user) <=0:
				results['status'] = False
				results['errors'].append('Something went wrong! Please try again.')
			elif len(postData['pw']) < 5 or postData['pw'] != user[0].password:
				results['status'] = False
				results['errors'].append('Something went wrong! Please try again.')
			else:
				results['user'] = user[0]
		return results

class User(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=75)
	email = models.CharField(max_length=25)
	password = models.CharField(max_length=20)
	objects = UserManager()
