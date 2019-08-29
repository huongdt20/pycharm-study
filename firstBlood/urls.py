"""firstBlood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from myApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index),
    path('lab411/', views.lab411),
    path('tl1/',views.tl1),
    path('tl2/',views.post, name='post_'),
    path('test/',views.test),
    path('cloud/',views.select)

]
