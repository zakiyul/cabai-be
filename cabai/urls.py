from django.urls import path
from . import views

urlpatterns = [
    path('gejala/', views.gejala_list),
    path('penyakit/', views.penyakit_list),
    path('basis-pengetahuan/', views.basispengetahuan_list)
]