from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class IncomeCategory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="income_categories",
    )
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table = "tracker_income_category"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="tracker_uniq_income_category_user_name",
            )
        ]
        ordering = ["name"]
        verbose_name = "категория дохода"
        verbose_name_plural = "категории доходов"

    def __str__(self) -> str:
        return self.name
