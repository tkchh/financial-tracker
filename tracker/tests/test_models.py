import pytest
from django.db import IntegrityError

from tracker.models import ExpenseCategory


@pytest.mark.django_db
def test_unique_expense_category_per_user(user):
    with pytest.raises(IntegrityError):
        ExpenseCategory.objects.create(user=user, name="Дом")