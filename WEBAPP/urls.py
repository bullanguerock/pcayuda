from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('terminos/', views.terms, name='terms'),
    path('politica/', views.policy, name='policy'),
    path('add_client/', views.add_client, name='add_client'),
    path('', views.formtest, name='formtest'),
    path('<int:pk>/', views.form2, name='form2'),
    path('<int:pk>/contacto', views.form3, name='form3'),
    path('<int:pk>/newclient', views.new_client, name='new_client'),
    path('test/', views.test, name='test'),
    path('slider', views.slider, name='slider'),
]
