from django.conf.urls import url
from .views import PaymentPage, ValidationWebhook


urlpatterns = [
    url(r'^$', PaymentPage.as_view(), name='payment_page'),
    url(r'^validate/$', ValidationWebhook.as_view(), name='payment_validation'),
]
