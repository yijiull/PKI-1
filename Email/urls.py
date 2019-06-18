from django.urls import path
from . import views

app_name = 'Email'

urlpatterns = [

    path('', views.index, name='index'),
    path('writeEmail/postEmail/', views.postEmail, name='postEmail'),
    path('writeEmail/', views.writeEmail, name='writeEmail'),
    path('draftBox/', views.draftBox, name='draftBox'),
    path('sentEmail/', views.sentEmail, name='sentEmail')
]