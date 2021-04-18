from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import ContactForm
from main_app.models import Project, Gallery

# Create your views here.

def index(request):
    projects = Project.objects.all().order_by('-start_date')[:3]

    context = {
        'projects':projects,
    }

    return render(request,'main_web/index.html',context)

def about(request):
    return render(request,'main_web/about.html')

def about2(request):
    return render (request,'main_web/about2.html')

def services(request):
    return render(request,'main_web/services.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            website= form.cleaned_data['website']
            message = form.cleaned_data['message']
            form.save()
            # try:
            #     send_mail(subject, from_email,message, ['isaac.maredi@gmail.com',from_email])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return redirect('index')

    return render(request, "main_web/contact.html", {'form': form})
