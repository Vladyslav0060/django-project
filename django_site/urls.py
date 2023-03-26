from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('raspberry_app.urls')),
    path('admin/', admin.site.urls),
]