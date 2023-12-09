from django.urls import path
from authentication.views import login, logout, flutter_register

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),path('logout/', logout, name='logout'),
    path('registerFlutter/', flutter_register, name='register-flutter'),
]