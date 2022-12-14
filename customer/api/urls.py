from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = router.urls