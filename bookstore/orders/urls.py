from django.urls import path
from . import views
from .views import place_order, my_orders

urlpatterns = [
    path('', views.my_orders, name='my_orders'),
    path('plcae/', place_order, name='place_order'),
]