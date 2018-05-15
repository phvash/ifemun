from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^special-event$', TemplateView.as_view(template_name='conference/special_event.html'), name='special-event'),
    url(r'^schedule$', TemplateView.as_view(template_name='conference/schedule.html'), name='schedule'),
    url(r'^speakers$', TemplateView.as_view(template_name='conference/speakers.html'), name='speakers'),
    url(r'^accomodation/$', TemplateView.as_view(template_name='conference/accomodation.html'), name='accomodation'),
]
