from django.contrib import admin
from django.urls import path, include
from LittleLemonAPI import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),
    path('api/',include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))

]
