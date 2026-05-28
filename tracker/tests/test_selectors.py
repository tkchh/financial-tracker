from datetime import date
from decimal import Decimal

import pytest

from tracker.models import Expense, Income
from tracker.selectors import build_expense_statistics, build_income_statistics


@pytest.mark.django_db
def test_build_expense_statistics(user, user_expense_category):
    Expense.objects.create(
        user=user,
        expense_category=user_expense_category,
        amount=Decimal("100.00"),
        spent_at=date(2026, 3, 10),
    )
    Expense.objects.create(
        user=user,
        expense_category=user_expense_category,
        amount=Decimal("50.00"),
        spent_at=date(2026, 3, 20),
    )

    stats = build_expense_statistics(user, date(2026, 3, 1), date(2026, 3, 31))

    assert stats["total"] == Decimal("150")
    assert stats["breakdown_by_category"][0]["category_name"] == "Продукты"
    assert stats["chart"]["values"] == [150.0]


@pytest.mark.django_db
def test_build_income_statistics(user, user_income_category):
    Income.objects.create(
        user=user,
        income_category=user_income_category,
        amount=Decimal("3000.00"),
        received_at=date(2026, 3, 5),
    )

    stats = build_income_statistics(user, date(2026, 3, 1), date(2026, 3, 31))

    assert stats["total"] == Decimal("3000")
    assert stats["chart"]["values"] == [3000.0]