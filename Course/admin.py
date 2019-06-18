from django.contrib import admin

# Register your models here.

from .models import Course, SC, User

admin.site.register(User)
admin.site.register(Course)
admin.site.register(SC)