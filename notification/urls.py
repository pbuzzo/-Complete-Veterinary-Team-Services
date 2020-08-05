from django.urls import path
from notification import views

urlpatterns = [
    path('notifications/', views.get_notifications, name='notify')
]
