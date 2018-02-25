from django import forms

from .models import Applicant

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Delegate
        fields = ('first_name', 'last_name', 'department', 'part')