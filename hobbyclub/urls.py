from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
   	#url('', 'articles.urls'),
   	#path(r'about/', include('articles.urls')),
	#path(r'/', include('articles.urls')),		this wont work
	path(r'articles/', include('articles.urls')),
	path(r'', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)