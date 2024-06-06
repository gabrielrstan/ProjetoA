from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'user/pages/home.html'
