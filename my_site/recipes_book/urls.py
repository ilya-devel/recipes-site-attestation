from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('recipe/<int:id>/', views.recipe_info, name='recipe'),
]
