from django.shortcuts import render, redirect, HttpResponse
from models import User
from django.contrib import messages

def index(request):
	return render(request, 'login_app/index.html')

def register(request):
	results = User.objects.registerValidation(request.POST)
	if results ['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
	else: 
		user = User.objects.create(first_name = request.POST['firstnm'], last_name = request.POST['lastnm'], email = request.POST['email'], password = request.POST['pw'])
		messages.success(request, 'User has been created.')
	return redirect('/')

def login(request):
	results = User.objects.loginValidation(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['first_name'] = results['user'].first_name
	request.session['last_name'] = results['user'].last_name
	request.session['user_id'] = results['user'].id


	return redirect('/wall')



