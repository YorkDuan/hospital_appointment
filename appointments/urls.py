import django.urls
from .views import doctor_list, appointment_list

app_name = 'appointments'

urlpatterns = [
    django.urls.path('doctors/', doctor_list, name='doctor_list'),
    django.urls.path('appointments/', appointment_list, name='appointment_list'),
]
