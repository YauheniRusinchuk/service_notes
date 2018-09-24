from django.urls import path
from settings.views import index, change


app_name = 'settings'

urlpatterns = [
    path('', index, name='settings'),
    path('change/', change, name='change'),
]
