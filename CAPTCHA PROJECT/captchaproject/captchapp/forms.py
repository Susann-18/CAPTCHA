from django import forms
from captcha.fields import CaptchaField

class MyForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    captcha = CaptchaField()
