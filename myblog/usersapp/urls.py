from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main page'),
    path('profile/<str:username>/', views.profile_page),
    path('about/', views.about, name='about'),
    path('set-password/', views.set_password),
    path('set-userdata/', views.set_userdata),
    path('deactivate/', views.deactivate),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),
]