from django.urls import path
from .views import CadastroView, IndexView, DashView, AddManualView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('dashboard/', DashView.as_view(), name='dashboard'),
    path('addNovaSenhaM/', AddManualView.as_view(), name='addNovaSenhaM')
]   