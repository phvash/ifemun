from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.RegistrationPage.as_view(), name='reg-form'),
    url(r'^submit$', views.RegistrationSubmit.as_view(), name='reg-submit'),
]
