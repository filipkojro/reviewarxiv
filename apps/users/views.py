from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TestViewUsers(TemplateView):
    template_name = 'reviews/test.html'