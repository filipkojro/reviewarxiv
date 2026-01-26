from django.views.generic import TemplateView, DetailView, CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy


# Create your views here.
class TestViewUsers(TemplateView):
    template_name = "users/users_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["users"] = CustomUser.objects.all()

        return context


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"

    slug_field = "username"
    slug_url_kwarg = "username"


class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
