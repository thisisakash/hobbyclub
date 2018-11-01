from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#handler404 = 'articles.views.handler404'
#handler500 = 'articles.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'articles/', include('articles.urls')),
    path(r'accounts/', include('accounts.urls')),
    #include('password_reset.urls')
   	#url('', 'articles.urls'),
   	#path(r'about/', include('articles.urls')),
	#path(r'/', include('articles.urls')),		this wont work
	path('', include('django.contrib.auth.urls'))
	
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)