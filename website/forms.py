from django import forms
from .models import BetaRequest
from captcha.fields import ReCaptchaField

class BetaRequestForm(forms.ModelForm):

    class Meta:
        model = BetaRequest
        fields = ('name', 'phone', 'email', 'requirements')

