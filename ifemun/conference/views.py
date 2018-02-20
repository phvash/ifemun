from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import RegistrationForm


class RegistrationPage(TemplateView):
    def get(self, request, **kwargs):
        form = RegistrationForm()
        template_path = "conference/registration.html"
        return render(request, template_path, {'form': form})

    def post(self, request, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            delegate = form.save(commit=False)
            delegate.save()
            # update this to point to success message
            return redirect('conference:post_reg')
        else:
            form = RegistrationForm()
            return render(request, template_path, {'form': form})