from django.urls import path
from divulgar import views

urlpatterns = [
    path('divulgar/', views.divulgar, name="divulgar"),
]