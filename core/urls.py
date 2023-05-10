from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('registration/', views.registration, name = 'registration'),
    path('parade_state/', views.parade_state, name = 'parade state'),
    path('bpet_ppt/', views.bpet_ppt, name = 'bpet / ppt'),
    path('mob_coln/', views.mob_coln, name = 'mob coln'),
]
