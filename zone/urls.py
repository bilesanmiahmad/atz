from django.urls import path

from zone import views

urlpatterns = [
    path('', views.index, name='index'),
]