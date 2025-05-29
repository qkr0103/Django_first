from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),#127.0.0.1:8000/admin/
    path("polls/",include("polls.urls")),
]
