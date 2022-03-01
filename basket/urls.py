from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_stuff, name='basket_stuff'),

]