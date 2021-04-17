from django.urls import path 
from . import views

app_name = 'main_users'

urlpatterns =[
    path('register',views.register, name = 'register'),
    path('login',views.login, name = 'login'),
]