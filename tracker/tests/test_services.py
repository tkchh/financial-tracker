from datetime import date
from decimal import Decimal

import pytest

from tracker.models import Expense, Income
from tracker.services import (
    calculate_balance,
    create_default_expense_categories,
    create_default_income_categories,
    get_current_month_range,
    get_month_range,
)


@pytest.mark.django_db
def test_create_default_expense_categories(user):
    create_default_expense_categories(user)
    assert user.expense_categories.count() == 9


@pytest.mark.django_db
def test_create_default_income_categories(user):
    create_default_income_categories(user)
    assert user.income_categories.count() == 3


@pytest.mark.django_db
def test_get_month_range():
    start, end = get_month_range(2026, 2)
    assert start == date(2026, 2, 1)
    assert end == date(2026, 2, 28)


@pytest.mark.django_db
def test_get_current_month_range():
    start, end = get_current_month_range(date(2026, 5, 15))
    assert start == date(2026, 5, 1)
    assert end == date(2026, 5, 31)


@pytest.mark.django_db
def test_calculate_balance(user, user_expense_category, user_income_category):
    Income.objects.create(
        user=user,
        income_category=user_income_category,
        amount=Decimal("1000.00"),
        received_at=date.today(),
    )
    Expense.objects.create(
        user=user,
        expense_category=user_expense_category,
        amount=Decimal("250.00"),
        spent_at=date.today(),
    )

    result = calculate_balance(user, date.today(), date.today())

    assert result["total_income"] == Decimal("1000")
    assert result["total_expense"] == Decimal("250")
    assert result["balance"] == Decimal("750")