# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import QuestionAnswer

class QAAdmin(admin.ModelAdmin):
	list_display = ['question', 'answer']

admin.site.register(QuestionAnswer, QAAdmin)
