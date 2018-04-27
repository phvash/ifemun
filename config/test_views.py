from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone


from ifemun.registration.forms import RegistrationForm
from ifemun.blog.models import Post



class MyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MyView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        # <view logic>
        return HttpResponse('get result')
    @csrf_exempt
    def post(self, request):
        return HttpResponse('post result')

class RegistrationSubmit(TemplateView):
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

def regformfunction(request):
    if request.method == "POST":
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

def admin_view(request):
    return redirect('https://ifemun.herokuapp.com/somelocation/login/')

def home_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    template_path = "pages/new_home.html"
    return render(request, template_path, {'posts': posts[len(posts)-2:len(posts)]})
