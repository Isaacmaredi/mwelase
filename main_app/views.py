from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, Gallery


class PortfolioListView(ListView):
    model = Project
    template_name ='main_app/portfolio.html'
    
class GalleryListView(ListView):
    model = Gallery
    template_name ='main_app/gallery.html'