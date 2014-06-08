from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from .models import User


class RegisterView(CreateView):
    model = User
    fields = ("email", "username", "password")
    template_name = "profiles/register.html"

    def get_success_url(self):
        return reverse('profiles:detail', args=(self.object.id,))



class ProfileDetailView(CreateView):
    model = User
    fields = ("email", "username", "password")
    template_name = "profiles/register.html"


class ProfileEditView(CreateView):
    model = User
    fields = ("email", "username", "password")
    template_name = "profiles/register.html"
