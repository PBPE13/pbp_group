from django.urls import path
from main.views import show_main
from main.views import register, login_user, logout_user, show_home, profile_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', show_home, name='home'),
    path('profile/', profile_user, name='profile_user'),
]