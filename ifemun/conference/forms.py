from django import forms

from .models import Delegate

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Delegate
        fields = ('first_name', 'last_name', 'department')