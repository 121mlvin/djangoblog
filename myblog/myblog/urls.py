from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('usersapp.urls')),
    path('', include('topicsapp.urls')),
    path('', include('articlesapp.urls')),
    path('admin/', admin.site.urls),
]
