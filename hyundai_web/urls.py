"""hyundai_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from hyundai_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('models/', views.models, name='models'),
    path('service/', views.service, name='service'),
    path('stock/', views.stock, name='stock'),
    path('testdrive/', views.testdrive, name='testdrive'),



#######################  RU   ################################

    path('ru/', views.ru_index, name='ru_index'),
    path('ru/about/', views.ru_about, name='ru_about'),
    path('ru/contact/', views.ru_contact, name='ru_contact'),
    path('ru/models/', views.ru_models, name='ru_models'),
    path('ru/service/', views.ru_service, name='ru_service'),
    path('ru/stock/', views.ru_stock, name='ru_stock'),
    path('ru/testdrive/', views.ru_testdrive, name='ru_testdrive'),    

]



handler404= "hyundai_web.views.not_found"