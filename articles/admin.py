from django.contrib import admin
from .models import Teammembers, Posts, Departments, Components
from .models import TextFile

admin.site.register(Teammembers)
admin.site.register(Posts)
admin.site.register(Departments)
admin.site.register(Components)
admin.site.register(TextFile)