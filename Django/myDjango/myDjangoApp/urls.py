from django.urls import path
from . import views
urlpatterns = [
    path('', views.appHome, name = "appHome"),
    path('<int:description_id>/', views.appDescription, name = "appDescription"),
]