from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('meal/new/', views.new_meal, name="new_meal"),
    path('meal/add/', views.add_meal, name="add_meal"),
    path('meal/edit/<int:meal_id>/', views.edit_meal, name="edit_meal"),
]
