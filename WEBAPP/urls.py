from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('terminos/', views.terms, name='terms'),
    path('politica/', views.policy, name='policy'),
    path('add_client/', views.add_client, name='add_client')
]
