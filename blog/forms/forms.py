

from django import forms
from blog.models.models import SearchSubject, InputSearch,VoteByUser,Contactmodel

class searchFormSubject(forms.ModelForm):
    class Meta:
        model = SearchSubject
        fields = ['Tag_field']
class SearchFormInput(forms.ModelForm):
    class Meta:
        model = InputSearch
        fields = ['custom_input']

class VoteByUserForm(forms.ModelForm):
    class Meta:
        model = VoteByUser
        fields = ['custom_field','id_field']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contactmodel
        fields = ['name','email','subject','message']

