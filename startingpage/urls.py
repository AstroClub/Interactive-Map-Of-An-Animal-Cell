from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='startingpage'),
    path('lysosomes.html', views.lysosomes, name='lysosomes'),
    path('ribosomes.html', views.ribosomes, name='ribosomes'),
    path('nucleus.html', views.nucleus, name='nucleus'),
    path('ER.html', views.ER, name='ER'),
    path('golgiapparatus.html', views.golgiapparatus, name='golgiapparatus'),
    path('mitochondria.html', views.mitochondria, name='mitochondria'),
    path('vacuoles.html', views.vacuoles, name='vacuoles'),
]