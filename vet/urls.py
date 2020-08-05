from django.urls import path
from vet import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('vet/<int:id>', views.vet, name='vet_page'),
    path('vet/<int:id>/edit/', views.edit_vet, name='edit_vet'),
    path('addvet/', views.addvet),
    path('addservice/', views.add_service, name='add_service'),
]