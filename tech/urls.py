from django.urls import path
from tech import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('tech/<int:id>', views.TechView.as_view(), name='tech_page'),
    path('tech/<int:id>/edit/', views.edit_tech, name='edit_tech'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup),
    path('signout/', views.signout),
    # path('404', views.FourView.as_view()),
    # path('500', views.FiveView.as_view()),
]