from django.urls import path

from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist_page, name='wishlist_page'),
    path('add/', views.wishlist_add, name='wishlist_add'),
    path('delete/', views.wishlist_delete, name='wishlist_delete'),
]