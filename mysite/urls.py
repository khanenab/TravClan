"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url, include
from rest_framework import routers, viewsets

from personal.models import Wallet
from personal.models import Transaction 

from personal.serializers import WalletSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
