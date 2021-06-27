from django.urls import path
from . import views

urlpatterns = [
    path('', views.homey, name="homey"),
    path('about/', views.aboutly, name="aboutly"),
    path('contact/', views.contactly, name="contactly")
]
