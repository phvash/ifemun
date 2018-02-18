from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import RegistrationForm


class RegistrationPage(TemplateView):
    def get(self, request, **kwargs):
        form = RegistrationForm()
        template_path = "conference/registration.html"
        return render(request, template_path, {'form': form})
