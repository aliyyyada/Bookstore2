from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('profile/', profile_view, name='profile_view'),
    #path('password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
]