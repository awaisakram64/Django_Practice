from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main',views.main, name='main'),
    #path('main/ava',views.main, name='2main')
]