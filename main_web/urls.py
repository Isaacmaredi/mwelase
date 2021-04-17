from django.urls import path
from . import views

app_name = 'main_web'

urlpatterns =[
    path('about/',views.about, name='about'),
    path('about2', views.about2, name='about2'),
    path('services/',views.services, name='services'),
    path('contact/',views.contact, name='contact'),
    # path('success/',views.success, name='success'),
]


