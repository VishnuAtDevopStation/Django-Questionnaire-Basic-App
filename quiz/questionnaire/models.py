# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class QuestionAnswer(models.Model):
	question = models.CharField(max_length=200, db_index=True)
	answer = models.CharField(max_length=200, db_index=True)
	option1 = models.CharField(max_length=200, db_index=True)
	option2 = models.CharField(max_length=200, db_index=True)
	option3 = models.CharField(max_length=200, db_index=True)

	class Meta:
		ordering = ('question',)
	
	def __str__(self):
	 	return self.question
