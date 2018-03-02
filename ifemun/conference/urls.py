from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^register$', views.RegistrationPage.as_view(), name='registration'),
    url(r'^$', TemplateView.as_view(template_name='conference/home.html'), name='conference-home'),
]
