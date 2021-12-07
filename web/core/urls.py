from django.urls import path
from .views import CadastroView, IndexView, DashView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('dashboard/', DashView.as_view(), name='dashboard')
]   