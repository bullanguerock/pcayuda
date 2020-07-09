from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('terminos/', views.terms, name='terms'),
    path('politica/', views.policy, name='policy'),
    path('add_client/', views.add_client, name='add_client'),
    path('test/', views.formtest, name='formtest'),
    path('test/<int:pk>/', views.form2, name='form2'),
    path('test/<int:pk>/contacto', views.form3, name='form3'),
    path('test/<int:pk>/newclient', views.new_client, name='new_client'),
    path('slider', views.slider, name='slider'),
]
