from django.contrib import admin
from django.urls import path
from .views import circle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',circle),
]