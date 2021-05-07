from django import forms
from django.core.validators import MaxValueValidator,MinValueValidator
class signupform(forms.Form):
    phone_number = forms.IntegerField(required=True,validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])

class signup2form(forms.Form):
    phone_number = forms.IntegerField(required=True,validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])
    username = forms.CharField(required=True,max_length=100)

class signup3form(forms.Form):
    phone_number = forms.IntegerField(required=True,validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])
    username = forms.CharField(required=True,max_length=100)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)



