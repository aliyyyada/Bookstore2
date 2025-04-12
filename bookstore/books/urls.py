from django.urls import path
from .views import book_list, book_create, book_update, book_delete


urlpatterns = [
    path('', book_list, name='book_list'),
    path('new/', book_create, name='book_create'),
    path('<int:pk>/edit/', book_update, name='book_update'),
    path('<int:pk>/delete/', book_delete, name='book_delete'),


]
