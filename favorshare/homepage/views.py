from django.views.generic.base import TemplateView


class HomepageIndexView(TemplateView):

    template_name = "homepage/index.html"
