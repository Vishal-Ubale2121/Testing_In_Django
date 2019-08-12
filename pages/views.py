from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
import ipdb
ipdb.set_trace()

class AboutPageView(TemplateView):
    template_name = 'about.html'


