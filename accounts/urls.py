from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login, logout, password_reset, password_reset_done
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
	url(r'^check/$', views.check, name="check"),
	#url(r'^signup/$', views.signup_view, name="signup"),
	url(r'^signup/$', views.signup, name="signup"),
	url(r'^login/$', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),

	url(r'^password_reset/$', auth_views.password_reset, name='reset_password'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

 	path(r'^$', include('django.contrib.auth.urls')),
    #instead of including above 4 urls, u can use the below one url 
    #url('^', include('django.contrib.auth.urls')),
]