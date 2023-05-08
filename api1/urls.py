from django.contrib import admin
from django.urls import path,include
from api1.views import companyViewSet,EmployeeViewSet
from rest_framework import routers
routers = routers.DefaultRouter()
routers.register(r'companies',companyViewSet)
routers.register(r'employee',EmployeeViewSet)

urlpatterns = [
    path('',include(routers.urls))
]
