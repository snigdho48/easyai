from django.urls import path
from django.contrib.auth import views as authentication_views
from users import forms
from . import views

app_name='users'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html', authentication_form=forms.UserLoginForm), name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]