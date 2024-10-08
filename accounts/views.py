from django.urls import reverse_lazy as _
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = _("login")
    template_name = "registration/signup.html"
