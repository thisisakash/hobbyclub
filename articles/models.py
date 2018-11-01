from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Teammembers(models.Model):
	DEPARTMENTS = (
        ('CE', 'Civil Engineering'),
        ('AM', 'AeroModelling'),
        ('RO', 'Robotics'),
        ('CS', 'Computer Science'),
        ('NO', 'None'),
    )

	name = models.CharField(max_length=100)
	department = models.CharField(default='NO', max_length=2, choices=DEPARTMENTS)
	currentyear = models.IntegerField()
	passingyear = models.IntegerField()
	thumb = models.ImageField(default='default.png', blank=True)
	
	def __str__(self):
		return self.name

class Posts(models.Model):
	DEPARTMENTS = (
        ('CE', 'Civil Engineering'),
        ('AM', 'AeroModelling'),
        ('RO', 'Robotics'),
        ('CS', 'Computer Science'),
        ('NO', 'None'),
    )

	author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, default="title")
	department = models.CharField(default='NO', max_length=2, choices=DEPARTMENTS)
	created_date = models.DateTimeField(default=timezone.now)
	short_des = models.TextField(default="short description")
	content = models.TextField(default="content")

	def __str__(self):
		return self.content

class Departments(models.Model):
	DEPARTMENTS = (
        ('CE', 'Civil Engineering'),
        ('AM', 'AeroModelling'),
        ('RO', 'Robotics'),
        ('CS', 'Computer Science'),
        ('NO', 'None'),
    )

	department = models.CharField(default='NO', max_length=2, choices=DEPARTMENTS)
	thumb = models.ImageField(default='default.png', blank=True)
	slogan = models.TextField(default="slogan")
	given_by = models.CharField(max_length=100)
	short_des = models.TextField(default="short description")
	long_des = models.TextField(default="long description")

	def __str__(self):
		return self.department

class Components(models.Model):
	BRANCHES = (
        ('CE', 'Civil Engineering'),
        ('CS', 'Computer Science Engineering'),
        ('EE', 'Electrical Engineering'),
        ('EL', 'Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('IT', 'Information Technology'),
        ('NO', 'Not Mentioned'),
    )

	name = models.CharField(max_length=100)
	person_taken = models.CharField(max_length=100)
	branch = models.CharField(default='NO', max_length=2, choices=BRANCHES)
	year = models.IntegerField()
	borrow_date = models.DateTimeField(default=timezone.now)
	return_date = models.DateTimeField(blank=True, null=True)

class TextFile(models.Model):
    # if storing in filesystem
    content = models.FileField()
