from django.urls import path
from .views import index, login_view, patient_dashboard, doctor_dashboard

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login_view, name='login'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
]
