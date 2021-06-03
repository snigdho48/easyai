"""easyai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
#from django.contrib.auth import views as authentication_views

#https://docs.djangoproject.com/en/3.1/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static

from users import forms 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('analytics/',include('analytics.urls')),
    #path('login/',authentication_views.LoginView.as_view(template_name='users/login.html', authentication_form=forms.UserLoginForm), name='login'),
    #path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    #path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
