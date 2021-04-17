from django.urls import path
from main_app.views import  PortfolioListView, GalleryListView

app_name = 'main_app'

urlpatterns=[
    path('portfolio/',PortfolioListView.as_view(),name='portfolio'),
    path('gallery/',GalleryListView.as_view(),name='gallery'),
]
