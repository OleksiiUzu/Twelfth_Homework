from django.urls import path

from . import views

urlpatterns = [
    path('', views.animals, name='animals'),
    path('search', views.search, name='search'),
    path('sort/<sort_by>', views.animal_sort, name='animal_sort'),
    path('animal_id=<int:animal_id>', views.animal, name='animal'),
    path('animal_id=<int:animal_id>/schedule', views.schedule, name='schedule'),
]
