from django.urls import path
from testurlapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<int:index>', views.home, name='users')
]