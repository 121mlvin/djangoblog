from django.urls import path
from . import views

urlpatterns = [
    path('<int:article>/', views.article),
    path('<int:article>/comment/', views.article_comment),
    path('<int:article>/update/', views.article_update),
    path('<int:article>/delete/', views.article_delete),
    path('create/', views.create),

]