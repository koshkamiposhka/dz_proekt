from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tariff(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)  # можно использовать для окончания подписки

    def __str__(self):
        username = getattr(self.user, "username", "Unknown")
        tariff_name = getattr(self.tariff, "name", "Unknown")
        return f"{username} - {tariff_name}"


