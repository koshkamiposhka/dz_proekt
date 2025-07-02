from rest_framework.routers import DefaultRouter
from .views import TariffViewSet, UserSubscriptionViewSet

router = DefaultRouter()
router.register('tariffs', TariffViewSet, basename='tariff')
router.register('subscriptions', UserSubscriptionViewSet, basename='usersubscription')

urlpatterns = router.urls
