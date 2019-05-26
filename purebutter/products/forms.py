from django import forms

class SearchForm(forms.Form):
    research = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"autocomplete col-md-8"}))