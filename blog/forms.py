

from django import forms
from blog.models import SearchSubject, InputSearch

class searchFormSubject(forms.ModelForm):
    class Meta:
        model = SearchSubject
        fields = ['custom_field']
class SearchFormInput(forms.ModelForm):
    class Meta:
        model = InputSearch
        fields = ['custom_input']
