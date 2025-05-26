from django import forms
from blog.models import SearchTag
from .models import ContactUs 

class searchForm(forms.ModelForm):
    class Meta:
        model = SearchTag
        fields = ['tag_name','describ']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','email','subject','message']


