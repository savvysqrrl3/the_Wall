from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

class MessageManager(models.Manager):
	print 'hi'


class Message(models.Model):
	author = models.ForeignKey(User)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)	
	updated_at = models.DateTimeField(auto_now = True)
	objects = MessageManager()

class Comment(models.Model):
	author = models.ForeignKey(User)
	parent = models.ForeignKey(Message)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)	
	updated_at = models.DateTimeField(auto_now = True)
	objects = MessageManager()
	