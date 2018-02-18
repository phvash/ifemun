from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.RegistrationPage.as_view(), name='registration'),
]
