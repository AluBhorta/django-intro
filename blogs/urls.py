from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('add/', views.add_blog, name='add_form'),
    path('update/<int:id>/', views.update_blog, name='update_blog'),
    path('delete/', views.delete_blog, name='delete_blog')
]
