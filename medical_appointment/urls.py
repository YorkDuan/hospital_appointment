from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('appointments/', include('appointments.urls')),
    path('admin/', admin.site.urls),
]
