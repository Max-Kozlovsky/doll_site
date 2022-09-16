from django.urls import path
from . import views

urlpatterns = [
    path('interior_dolls_list', views.interior_dolls_list, name='interior_dolls_list'),
    path("interior_dolls/<int:pk>/", views.interior_doll_detail, name='interior_doll_detail'),
    path('for_game_list', views.for_game_list, name='for_game_list'),
    path("play_dolls/<int:pk>/", views.for_game_detail, name='for_game_detail'),
    path('toys_list', views.toys_list, name='toys_list'),
    path("toys/<int:pk>/", views.toys_detail, name='toy_detail'),
]
