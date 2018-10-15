from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Teammembers, Posts, Departments, Components
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers

def about(request):
	#return HttpResponse('about page')
	return render(request, 'articles/about.html')

def team(request):
	members = Teammembers.objects.all()
	return render(request, 'articles/members.html', {'members': members})

def homepage(request):
	return render(request, 'articles/homepage.html')

def post(request, pk):
	post = get_object_or_404(Posts, pk=pk)
	#post = Posts.objects.all()
	return render(request, 'articles/posts.html', {'post': post})

def deptcs(request):
	dept = Departments.objects.all().filter(department='CS')
	posts = Posts.objects.all().filter(department='RO')
	members = Teammembers.objects.all().filter(department='CE')
	return render(request, 'articles/deptcs.html', {'dept': dept, 'posts':posts, 'members':members	})
	#return HttpResponse('help me')

@login_required(login_url="/accounts/login/")
def article_create(request):
	return render(request, 'articles/article_create.html')

def departments(request):
	depts = Departments.objects.all()
	return render(request, 'articles/departments.html', {'depts': depts})

def components(request):
	return render(request, 'articles/components.html')

def validate_component(request, username):
	#component = request.GET.get('component', None)
	component = request.GET.get('component', None)
	print (username)
	comps = Components.objects.filter(name__contains=component)
	# data = {
	# 	'is_taken': Components.objects.filter(name__contains=component).exists()
	# }
	# data = {
	# 	'name' : comps[0].name,
	# 	'branch' : comps[0].branch
	# }
	#return JsonResponse(data)
	#comp_list = list(comps)
	#return JsonResponse(comp_list, safe=False)
	return JsonResponse(serializers.serialize('json', comps), safe=False)