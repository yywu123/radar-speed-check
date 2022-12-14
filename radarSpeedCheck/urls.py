
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import  static


urlpatterns = [
    path('', views.home, name='home'),

    path('detail/<str:pk>/', views.detail, name='detail'),
    path('createItem/',views.createItem, name = 'createItem'),
    path('updateItem/<str:pk>/', views.updateItem, name='updateItem'),
    path('deleteItem/<str:pk>/', views.deleteItem, name='deleteItem'),
    path('createTimeSheet/', views.createTimeSheet, name='createTimeSheet'),
    #path('createTimeSheet/<str:pk>/', views.createTimeSheet, name='createTimeSheet'),
    path('updateTimeSheet/<str:pk>/', views.updateTimeSheet, name='updateTimeSheet'),
    path('deleteTimeSheet/<str:pk>/', views.deleteTimeSheet, name='deleteTimeSheet'),
    path('detailView/<str:pk>/', views.detailView, name='detailView'),
    path('printPDF/<str:pk>/', views.printPDF, name='printPDF'),

    path('base/', views.base, name= 'base'),


]


