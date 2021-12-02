from django.urls import path
from .views import CadastroView, IndexView, BaseView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('base/', BaseView.as_view(), name='base')
]   