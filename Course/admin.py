from django.contrib import admin

# Register your models here.

from .models import Course, SC, User, Notice, Topic, Comment, Reply

admin.site.register(User)
admin.site.register(Course)
admin.site.register(SC)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Notice)
