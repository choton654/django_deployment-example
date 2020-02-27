from django import forms
from django.core import validators

class FromName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    v_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean_password(self):
        data = self.cleaned_data["password"]
        x = "_"
        if x not in data:
                raise forms.ValidationError( "!@#$%^&*_ must be in password")

        return data

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data["email"]
        v_email = cleaned_data["v_email"]

        if email != v_email:
            raise forms.ValidationError("EMAILS MUST BE SAME")
