from rest_framework import viewsets, permissions
from .models import Tariff, UserSubscription
from .serializers import TariffSerializer, UserSubscriptionSerializer
from rest_framework.permissions import IsAuthenticated

class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [permissions.AllowAny]

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserSubscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Для каждого пользователя только одна подписка, создаём или обновляем
        instance, created = UserSubscription.objects.update_or_create(
            user=self.request.user,
            defaults={'tariff': serializer.validated_data['tariff']}
        )
        self.instance = instance  # чтобы можно было вернуть объект, если нужно

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

