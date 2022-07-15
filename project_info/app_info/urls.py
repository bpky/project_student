
from django.urls import path
from . import views


urlpatterns = [
    path('users/dashboard/', views.User_dashboard, name="user.dashboard"),
   
]
