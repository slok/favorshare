from django.views.generic.base import TemplateView

from core.mixins import LoginRequiredMixin


class HomepageIndexView(LoginRequiredMixin, TemplateView):

    template_name = "homepage/index.html"
