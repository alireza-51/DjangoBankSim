from django.contrib import admin
from django.urls import path, include
from .views import BranchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'branch', BranchViewSet, basename='branch')

urlpatterns = router.urls
