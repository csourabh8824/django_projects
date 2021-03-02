import stripe

from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY

class MyView(TemplateView):
    template_name = "django_registration/base_template.html"
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request, 'django_registration/charge.html')