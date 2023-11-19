from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.topics),
    path('topics/<str:topic>/subscribe/', views.topics_subscribe),
    path('topics/<str:topic>/unsubscribe/', views.topics_unsubscribe),

]