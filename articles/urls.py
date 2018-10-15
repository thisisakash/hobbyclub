from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
	url(r'^about/$', views.about),
	url(r'^team/$', views.team),
	url(r'^homepage/$', views.homepage),
	url(r'^post/(\d)+/$', views.post),
	url(r'^dept/$', views.departments),
	url(r'^dept/cs/$', views.deptcs),
	#url(r'^dept/ro/$', views.deptro),
	#url(r'^dept/ce/$', views.deptce),
	#url(r'^dept/am/$', views.deptam),
	url(r'^create/$', views.article_create, name="create"),
	url(r'^components/$', views.components, name="components"),
	url(r'^ajax/validate_component/(?P<username>\w{0,50})$', views.validate_component, name="ajax_query"),	
]