from django import forms

class SearchForm(forms.Form):
    research = forms.CharField(label="")