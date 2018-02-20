from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^register$', views.RegistrationPage.as_view(), name='registration'),
    url(r'^success', TemplateView.as_view(template_name='conference/reg_success.html'), name='post_reg'),
]
