from django.urls import path
from unit import views

urlpatterns = [
    path('', views.home, name='home'),
]
