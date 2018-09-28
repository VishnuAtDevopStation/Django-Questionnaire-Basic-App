# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import QuestionAnswer

def list_view(request):
	"""
	Processing The Questions and their option view | also 
	responsible for handling the customer mark calculation logic
	"""
	qadata = QuestionAnswer.objects.all()
	qs_counter = 1
	an_counter = 0
	flag = False
	if request.method == "POST":
		print(request.POST)
		for qa in qadata:   
			form_field = 'optradio_'+str(qs_counter)
			print(form_field)
			answer = request.POST.get(form_field)
			print(answer)
			print('right ansr is')
			print(qa.answer)
			if qa.answer == answer:
				an_counter+=1
				flag = True
			qs_counter+=1
		result_message = ''
		if an_counter > 2:
			result_message = 'You Have Won The Exam'
		else:
			result_message = 'Failed! Better Luck Next Time'
		result = {
				'total_questions': qs_counter,
				'total_answers': an_counter,
				'result_message':result_message
				}
		return render(request, 'questionnaire/detail.html',{'result': result})
	return render(request, 'questionnaire/list.html',{'qadata': qadata})

def home_page(request):
	"""
	Processing Home Page View
	"""
	return render(request, 'questionnaire/home.html',{})

   