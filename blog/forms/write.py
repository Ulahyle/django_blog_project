from django import forms
from django.forms import ModelForm
from blog.models.models import CustomPost


class Write(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.IntegerField(min_value=0, max_value=5, required=True)
    tag = forms.CharField(max_length=100, required=True)