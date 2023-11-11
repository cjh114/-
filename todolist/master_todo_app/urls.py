from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createtodo/', views.createtodo, name='createtodo'),
    path('deletetodo/', views.deletetodo, name='deletetodo')
]
