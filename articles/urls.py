from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^departments/$', views.departments, name="departments"),
	url(r'^departments/am/$', views.deptam, name="deptam"),
	url(r'^departments/ce/$', views.deptce, name="deptce"),
	url(r'^departments/cs/$', views.deptcs, name="deptcs"),
	url(r'^departments/ro/$', views.deptro, name="deptro"),
	url(r'^departments/no/$', views.deptno, name="deptno"),
	url(r'^components/$', views.components, name="components"),
	
	url(r'^about/$', views.about),
	url(r'^team/$', views.team),
	
	url(r'^post/(?P<id>\d{0,10})/$', views.post),
	
	
	#url(r'^dept/ro/$', views.deptro),
	#url(r'^dept/ce/$', views.deptce),
	#url(r'^dept/am/$', views.deptam),
	url(r'^create/$', views.article_create, name="create"),
	
	url(r'^componentsnew/$', views.componentsnew, name="componentsnew"),
	url(r'^ajax/validate_component/(?P<username>\w{0,50})$', views.validate_component, name="ajax_query"),	
	url(r'^textfileopen/$', views.textfileopen),
]