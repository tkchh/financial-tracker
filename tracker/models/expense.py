from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from .expense_category import ExpenseCategory

User = get_user_model()


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses",
    )
    expense_category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.PROTECT,
        related_name="expense_records",
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    spent_at = models.DateField()
    comment = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tracker_expense"
        ordering = ["-spent_at", "-id"]
        indexes = [
            models.Index(
                fields=["user", "spent_at"],
                name="trk_exp_user_date_idx",
            ),
            models.Index(
                fields=["user", "expense_category"],
                name="trk_exp_user_cat_idx",
            ),
        ]
        verbose_name = "расход"
        verbose_name_plural = "расходы"

    def __str__(self) -> str:
        return f"{self.expense_category}: {self.amount}"
