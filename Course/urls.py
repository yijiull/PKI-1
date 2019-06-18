from django.urls import path
from . import views

app_name = 'Course'

urlpatterns = [
    #ex: /course/
    path('', views.index, name='index'),
    #ex: /course/login/
    path('login/', views.login, name='login'),
    #ex: /course/login_verify/
    path('login_verify/', views.login_verify, name='login_verify'),

]
