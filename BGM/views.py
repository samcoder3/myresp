from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from .models import Post,Profile,Comment

# Create your views here.


def index(request):
	return render(request,'index.html')

class PostList(ListView):
	model=Post
	ordering=['-id']
	template_name='ourservice.html'
	

def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html') 
def Stuff(request):
	return render(request,'stuff.html')

class Addcomments(CreateView):
	model=Comment
	template_name='addcomment.html'
	fields='__all__'
from django.shortcuts import render

# Create your views here.
