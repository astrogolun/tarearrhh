
from django.contrib import admin
from django.urls import path
from empleadosapp import views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('results/', views.vista_filtro, name='filtro'),
    path('signin/', views.signin, name='signin'),
    path('error/', views.vista_filtro, name='error')



    
]
