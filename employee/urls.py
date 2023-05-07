from django.urls import path

from .views import show_employees


urlpatterns = [
    path('', show_employees, name='show_employees'),
]

