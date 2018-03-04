from django.contrib import admin

# Register your models here.

from .models import Question,Network

admin.site.register(Question)
admin.site.register(Network)