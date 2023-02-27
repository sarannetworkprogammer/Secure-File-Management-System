from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='filemgmt-home'),
    path('dashboard/', views.dashboard, name='filemgmt-dashboard'),
    path('cd/', views.cd, name='cd'),
    path('md/', views.md, name='md'),
    path('mf/', views.mf, name='mf'),
    path('rmdir/', views.rmdir, name='rmdir'),
    path('rm/', views.rm, name='rm'),
    path('view/', views.view, name='view'),
    path('upload', views.upload, name='upload')
]
