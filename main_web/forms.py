from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    website = forms.URLField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)