from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from .income_category import IncomeCategory

User = get_user_model()


class Income(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="incomes",
    )
    income_category = models.ForeignKey(
        IncomeCategory,
        on_delete=models.PROTECT,
        related_name="income_records",
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    received_at = models.DateField()
    comment = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tracker_income"
        ordering = ["-received_at", "-id"]
        indexes = [
            models.Index(
                fields=["user", "received_at"],
                name="trk_inc_user_date_idx",
            ),
            models.Index(
                fields=["user", "income_category"],
                name="trk_inc_user_cat_idx",
            ),
        ]
        verbose_name = "доход"
        verbose_name_plural = "доходы"

    def __str__(self) -> str:
        return f"{self.income_category}: {self.amount}"
