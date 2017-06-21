# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
	title = models.TextField()
	author = models.ForeignKey(Author)
	published_date = models.DateField()
	category = models.CharField(max_length=255)
	in_print = models.BooleanField()
