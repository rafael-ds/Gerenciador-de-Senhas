from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'


class CadastroView(TemplateView):
    template_name = 'cadastro.html'


class BaseView(TemplateView):
    template_name = 'base.html'