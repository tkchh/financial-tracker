from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ExpenseCategory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expense_categories",
    )
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table = "tracker_expense_category"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="tracker_uniq_expense_category_user_name",
            )
        ]
        ordering = ["name"]
        verbose_name = "категория расхода"
        verbose_name_plural = "категории расходов"

    def __str__(self) -> str:
        return self.name
