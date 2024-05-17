from atexit import register
from turtle import home
from django.urls import path
from django.contrib import admin
from fxd import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.register,name= 'register'),
    # path('login/',views.login,name='login'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('home/',views.home,name= 'home'),
    path('finds/',views.finds,name= 'finds'), 
    # path('sub/',views.subscriber)
    path('contact/',views.contact), 
    
    
]
