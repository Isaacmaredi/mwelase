from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from mainweb.models import Profile

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=250, required=True)
    last_name=forms.CharField(max_length=250)
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

# class ProfileCreationForm(forms.ModelForm):
    
#     class Meta:
#         model= Profile 
#         fields= '__all__'