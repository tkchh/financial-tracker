from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from tracker.services import (
    create_default_expense_categories,
    create_default_income_categories,
)

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_categories(sender, instance, created, **kwargs):
    if created:
        create_default_expense_categories(instance)
        create_default_income_categories(instance)
