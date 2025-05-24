

from django import forms
from blog.models import SearchTag

class searchForm(forms.ModelForm):
    class Meta:
        model = SearchTag
        fields = ['tag_name','describ']