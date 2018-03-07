from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import RegistrationForm

@method_decorator(csrf_exempt, name='post')
class RegistrationPage(TemplateView):
    def get(self, request, **kwargs):
        form = RegistrationForm()
        template_path = "conference/new_reg.html"
        return render(request, template_path, {'form': form})

    def post(self, request, **kwargs):
        form = RegistrationForm(request.POST)
        template_path = "conference/new_reg.html"
        if form.is_valid():
            delegate = form.save(commit=False)
            delegate.save()
            # update this to point to success message
            messages.success(request, 'Your registration was successful!')
            return redirect('home')
        else:
            # form = RegistrationForm()
            return render(request, template_path, {'form': form})


