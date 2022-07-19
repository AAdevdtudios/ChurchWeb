
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name="main"),
    path('about/', views.about_us, name="about"),
    path('locations/', views.location, name="location"),
    path('contactUs/', views.contact_us, name="contact"),
]
