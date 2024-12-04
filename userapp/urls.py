"""
from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
"""

from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [

    path('home/', views.home, name='home'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password-reset/', views.password_reset_view, name='password_reset'),
]
