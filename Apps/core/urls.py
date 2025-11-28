from django.urls import path

from Apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    ]