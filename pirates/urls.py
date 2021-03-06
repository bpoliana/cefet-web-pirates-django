from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaTesourosView.as_view(), name='list'),
    path('new', views.SalvarTesouroView.as_view(), name='new'),
    path('delete/<int:tr>', views.DeletarTesouroView.as_view(), name='delete'),
    path('edit/<int:tr>', views.SalvarTesouroView.as_view(), name='edit')
]
