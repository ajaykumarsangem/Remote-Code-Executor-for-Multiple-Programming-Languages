from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('update', views.update_user),
    path('get', views.get_user_by_email),
]
