from django.urls import path
from . import views

app_name = 'Course'

urlpatterns = [
    #ex: /course/
    path('', views.index, name='index'),
    #ex: /course/login/
    path('login/', views.login, name='login'),
    #ex: /course/login/verify/
    path('login/verify/', views.login_verify, name='login_verify'),
    #ex: /course/register/
    path('register/', views.register, name='register'),
    #ex: /course/register/verify/
    path('register/verify/', views.register_verify, name='register_verify'),
    #ex: /course/update_personal_info/verify
    path('update_personal_info/verify/', views.update_verify, name='update_verify'),
    #ex: /course/update_personal_info
    path('update_personal_info/<str:userid>/get/', views.update_personal_info, name='update_personal_info'),
    #ex: /course/upload_pic/201630610533
    path('upload_pic/<str:userid>/', views.upload_pic, name='upload_pic'),
    #ex: /course/<str:courseid>/info/
    path('<str:courseid>/info/', views.course, name='course_info'),
    #ex: /course/<str:filepath>/download/
    path('<str:filepath>/download/', views.download, name='download'),

]
