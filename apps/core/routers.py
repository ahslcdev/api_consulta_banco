from rest_framework.routers import DefaultRouter

from apps.core.viewsets import BankConsultViewSet

router = DefaultRouter()
router.register(r'banks', BankConsultViewSet)