from django.shortcuts import render, redirect, HttpResponse
from models import Message, User, Comment

def index(request):
	context = {
	"posts": Message.objects.all().order_by("-created_at"),
	"current_user": User.objects.get(id = request.session['user_id']),
	}
	return render(request, 'message_app/index.html', context)

def message(request):
	user = User.objects.get(id = request.session['user_id'])
	message = Message.objects.create(author = user, content = request.POST['message'])
	return redirect('/wall/')

def comment(request):
	user = User.objects.get(id = request.session['user_id'])
	current_message = Message.objects.get(id = request.POST['id'])
	comment = Comment.objects.create(author = user, parent = current_message, content = request.POST['comment'])
	return redirect('/wall/')
