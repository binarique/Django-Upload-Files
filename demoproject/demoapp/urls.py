
from . import views
from django.urls import path

urlpatterns = [
    path('upload/', views.uploadPhoto.as_view(), name="upload"),
]
