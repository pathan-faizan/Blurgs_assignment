from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.image),
    path('get/', views.getImage),
]
