from django.contrib import admin
from django.urls import path, include
from .views import sayHello, BookingViewSet
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booking', BookingViewSet,basename='booking' )

urlpatterns = [
    ##path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('api-token-auth/',  obtain_auth_token  ),
    path('',include(router.urls)),
    
]