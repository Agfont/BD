from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.test),
    path('i/', views.list_conflicts),
    path('ii/', views.dealers_and_armed_groups),
    path('iii/', views.top5_deads_conficts),
    path('iv/', views.top5_mediations_organizations),
    path('v/', views.top5_largest_armed_groups),
    path('vi/', views.countries_by_religious_conflicts),
    path('addChief', views.addMilitaryChief)
]