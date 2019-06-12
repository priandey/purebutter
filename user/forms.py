from django import forms


class SigninForm(forms.Form):
    email = forms.EmailField(label="Adresse e-mail", required=True)
    password = forms.CharField(
        label="Mot de Passe", required=True, widget=forms.PasswordInput)