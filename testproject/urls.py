
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ezra/', admin.site.urls),
    path('', include("testapp.urls")),
    path('settings', include("app2.urls"))

]
