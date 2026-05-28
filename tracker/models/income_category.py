from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class IncomeCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense_categories')
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name