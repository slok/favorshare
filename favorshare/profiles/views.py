from django.views.generic import CreateView

from .models import User


class RegisterView(CreateView):
    model = User
    fields = ("email", "username", "password")
    template_name = "profiles/register.html"

#    def render_to_response(self, context, **response_kwargs):
#        for k, v in context["form"].errors.items():
#            print(k)
#            print(type(v))
#            print("-" * 5)
#
#        for i in context["form"].errors["username"]:
#            print(i)
#        print(context["form"]["username"].label)
#        print(context["form"]["username"].name)
#        return super(RegisterView, self).render_to_response(context, **response_kwargs)
#    