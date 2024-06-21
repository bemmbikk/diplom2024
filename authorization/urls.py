from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'authorization'


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.register, name='register'),
]

