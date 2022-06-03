"""dismal_gateways_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from pages.views import homepage_view, contact_view, products_view, about_view
from products.views import album_detail_view, album_list_view
from redaction.views import article_list_view, article_detail_view

urlpatterns = [
    path('',homepage_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('products/', album_list_view, name = 'products'),
    path('album/<int:aid>/', album_detail_view, name='album'),
    path('about/', about_view, name='about'),
    path('redaction/', article_list_view, name='article_list'),
    path('article/<int:aid>/', article_detail_view, name='article_details')
        
]
