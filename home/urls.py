from django.urls import path
from django.contrib.auth import views as auth_views
from home.views import home, registration


app_name = 'home'

urlpatterns = [
    path('', home, name='homepage'),
    path('registration/', registration, name='registration'),
    path('login/', auth_views.login,  {'template_name': 'home/login.html'}, name='login_user'),
    path('logout/', auth_views.logout, {"next_page" : "/"}, name='logout')
]
