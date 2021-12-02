from django.urls import path
from .views import CadastroView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]   