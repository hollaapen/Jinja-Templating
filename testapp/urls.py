from django.urls import path

from . import views

app_name = "testapp"
urlpatterns = [

    path('', views.Test, name="Test"),
    path("contact/", views.contact, name="contact"),
    path('about/', views.about, name="about")

]
