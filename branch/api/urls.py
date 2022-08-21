from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet

router = DefaultRouter()
router.register(r'branch', BranchViewSet, basename='branch')

urlpatterns = router.urls
