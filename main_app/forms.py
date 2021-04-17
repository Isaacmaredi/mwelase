from django import forms
from django.forms import ModelForm 
from . import Project


class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields =['category','description','client','client',
                 'start_date',' end_date','status',
                 'progress_status,','status_date',
                 'image','value']
    
    
    