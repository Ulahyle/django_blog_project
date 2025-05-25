from django import forms


class Write(forms.Form):
    title  = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea)