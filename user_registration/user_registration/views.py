from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class MyView(View):

    def get(self, request, *args, **kwargs):
        # Displays Home page
        self.template_name = "django_registration/base_template.html"
        return render(request,self.template_name)
