from django import forms


class SearchForm(forms.Form):
    research = forms.CharField(label="", required=False, widget=forms.TextInput(
        attrs={"class": "autocomplete col-md-8"}))
