from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import Teammembers, Posts, Departments, Components
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers

from django.template import RequestContext

from .models import TextFile
import pyttsx3
from django.http import HttpResponse

def home(request):
	return render(request, 'articles/home.html')

def departments(request):
	depts = Departments.objects.all()
	return render(request, 'articles/departments.html', {'depts': depts})

def deptam(request):
	dept = Departments.objects.all().filter(department='AM')
	posts = Posts.objects.all().filter(department='AM')
	members = Teammembers.objects.all().filter(department='AM')
	return render(request, 'articles/departmentsingle.html', {'dept': dept, 'posts':posts, 'members':members})

def deptce(request):
	dept = Departments.objects.all().filter(department='CE')
	posts = Posts.objects.all().filter(department='CE')
	members = Teammembers.objects.all().filter(department='CE')
	return render(request, 'articles/departmentsingle.html', {'dept': dept, 'posts':posts, 'members':members})

def deptcs(request):
	dept = Departments.objects.all().filter(department='CS')
	posts = Posts.objects.all().filter(department='CS')
	members = Teammembers.objects.all().filter(department='CS')
	return render(request, 'articles/departmentsingle.html', {'dept': dept, 'posts':posts, 'members':members})

def deptro(request):
	dept = Departments.objects.all().filter(department='RO')
	posts = Posts.objects.all().filter(department='RO')
	members = Teammembers.objects.all().filter(department='RO')
	return render(request, 'articles/departmentsingle.html', {'dept': dept, 'posts':posts, 'members':members})
	#return HttpResponse('help me')

def deptno(request):
	return HttpResponse('no department selected')

def about(request):
	#return HttpResponse('about page')
	return render(request, 'articles/about.html')

def team(request):
	members = Teammembers.objects.all()
	return render(request, 'articles/members.html', {'members': members})

def components(request):
	comps = Components.objects.all()
	return render(request, 'articles/components.html', {'comps':comps})

def post(request, pk):
	post = get_object_or_404(Posts, pk=pk)
	#post = Posts.objects.all()
	return render(request, 'articles/posts.html', {'post': post})

# def post(request, id):
# 	return HttpResponse('this is the post number : ' + id)

@login_required(login_url="/accounts/login/")
def article_create(request):
	return render(request, 'articles/article_create.html')





def componentsnew(request):
	comps = Components.objects.all()
	return render(request, 'articles/componentsnew.html', {'comps':comps})

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

def handler404(request):
	return render(request, '404.html')

def handler500(request):
	return render(request, '500.html')

# def handler404(request, *args, **argv):
# 	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
# 	response.status_code = 404
# 	return response

# def handler500(request, *args, **argv):
# 	response = render_to_response('500.html', {}, context_instance=RequestContext(request))
# 	response.status_code = 500
# 	return response


def textfileopen(request):
    #files = TextFile.objects.all()
    #return HttpResponse(files)
    #return HttpResponse(files.content.read())
	f=open("C:/Users/tilliu/Desktop/website/hobbyclub/media/mydoc.txt", "r")
	contents = 'nothing read'
	if f.mode == 'r':
		contents =f.read()
	engine = pyttsx3.init()
	engine.say(contents);
	engine.setProperty('volume',0.9)
	engine.runAndWait()
	return HttpResponse(contents)
	