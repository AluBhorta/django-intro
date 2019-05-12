from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='index'),
    path('blog/details/<int:id>/', views.details, name='details'),
    path('details/<int:id>/', views.details, name='details'),
    path('blog/add/', views.add_blog, name='add_form'),
    path('blog/update/<int:id>/', views.update_blog, name='update_blog'),
    path('blog/delete/<int:id>/', views.delete_blog, name='delete_blog')
]
