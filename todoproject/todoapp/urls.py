from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classbase/',views.new.as_view(),name='classbase'),
    path('detailview/<int:pk>/',views.new3.as_view(),name='detailview'),
    path('deleteview/<int:pk>/',views.new2.as_view(),name='deleteview'),
    path('updateview/<int:pk>/',views.new1.as_view(),name='updateview'),


]