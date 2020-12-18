from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.test),
    path('2/conflict_form', views.conflict_form),
    path('2/military_chief_form', views.military_chief_form),
    path('2/political_leader_form', views.political_leader_form),
    path('2/armed_group_form', views.armed_group_form),
    path('2/division_form', views.division_form),
    path('2/organization_form', views.organization_form),
    path('2/weapon_form', views.weapon_form),
    path('2/dealer_form', views.dealer_form),
    path('i/', views.list_conflicts),
    path('ii/', views.dealers_and_armed_groups),
    path('iii/', views.top5_deads_conficts),
    path('iv/', views.top5_mediations_organizations),
    path('v/', views.top5_largest_armed_groups),
    path('vi/', views.countries_by_religious_conflicts),
    path('create-db', views.create_db),
]