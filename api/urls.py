from django.urls import path, include
from rest_framework import routers
from api import views

routers = routers.DefaultRouter()
routers.register(r'programmer', views.ProgrammerViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
