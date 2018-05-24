from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ifemun.registration.models import Applicant

import json


def str_hook(obj):
    return {k.encode('utf-8') if isinstance(k,unicode) else k :
            v.encode('utf-8') if isinstance(v, unicode) else v
            for k,v in obj}


class PaymentPage(TemplateView):
    def get(self, request, **kwargs):
        template_path = "payment/payment_page.html"
        return render(request, template_path)

class ValidationWebhook(TemplateView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ValidationWebhook, self).dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        template_path = "404.html"
        return render(request, template_path)

    def post(self, request, **kwargs):
        data = json.loads(request.body, object_pairs_hook=str_hook)
        print(data)
        email = data['data']['customer']['email']
        amount = data['data']['amount'] # in kobo
        payment_type = 'Observer' if amount == 300000 else "Delegate" 
        print(email, amount, payment_type)
        user = Applicant.objects.filter(email=email).first()
        print(user)
        if user and data['data']['status'] == 'success':
            user.amount_paid = kobo2naira(amount)
            user.payment_type = payment_type
            if payment_type == 'Delegate':
                user.package = determine_package(amount)
            user.save()
        return JsonResponse({"status": 200})


def determine_package(amount):
    if amount == 1500000:
        return "Gamma"
    elif amount == 1000000:
        return "Beta"
    elif amount == 850000:
        return "Alpha"
    elif amount == 650000:
        return "Delta"

def kobo2naira(amount):
    if amount == 1500000:
        return "15,000"
    elif amount == 1000000:
        return "10,000"
    elif amount == 850000:
        return "8,500"
    elif amount == 650000:
        return "6,500"
    elif amount == 300000:
        return "3,000"
