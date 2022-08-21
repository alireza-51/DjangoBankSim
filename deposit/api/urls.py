from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepositViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'deposit', DepositViewSet, basename='deposit')
router.register(r'loan', LoanViewSet, basename='loan')

urlpatterns = router.urls