from django.urls import path
from . import views

# Define URL patterns for myDjangoApp
urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:detail_id>/', views.detail, name="detail"),
] 