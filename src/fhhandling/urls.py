from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet


router = routers.DefaultRouter()
router.register(r"upload", UploadViewSet, basename="fhhandling")

urlpatterns = [path("", include(router.urls))]
