from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fish/', views.fishAll, name='fishAll'),
    path('fish/<str:name>/', views.fish, name='fish'),
    path('insect/', views.insectAll, name='insectAll'),
    path('insect/<str:name>/', views.insect, name='insect'),
    path('north/<str:name>/', views.north, name='north'),
    path('south/<str:name>/', views.south, name='south'),
]