from django.shortcuts import render
from django.views.generic import TemplateView

from .models import CustomUser

# Create your views here.
class TestViewUsers(TemplateView):
    template_name = 'users/users_list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['users'] = CustomUser.objects.all()

        return context

