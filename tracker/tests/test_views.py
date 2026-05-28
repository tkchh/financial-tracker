from datetime import date
from decimal import Decimal

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from tracker.models import Expense, ExpenseCategory, Income, IncomeCategory


@pytest.mark.django_db
def test_signup_creates_default_categories(client):
    response = client.post(
        reverse("signup"),
        {
            "username": "new_user",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
        },
    )

    assert response.status_code == 302
    user = User.objects.get(username="new_user")
    assert ExpenseCategory.objects.filter(user=user).count() == 9
    assert IncomeCategory.objects.filter(user=user).count() == 3


@pytest.mark.django_db
def test_expense_crud(auth_client, user, user_expense_category):
    create_resp = auth_client.post(
        reverse("expense-create"),
        {
            "expense_category": user_expense_category.id,
            "amount": "100.00",
            "spent_at": date.today(),
            "comment": "Обед",
        },
    )
    assert create_resp.status_code == 302

    expense = Expense.objects.get(user=user)

    update_resp = auth_client.post(
        reverse("expense-update", args=[expense.id]),
        {
            "expense_category": user_expense_category.id,
            "amount": "130.00",
            "spent_at": date.today(),
            "comment": "Обед и кофе",
        },
    )
    assert update_resp.status_code == 302

    delete_resp = auth_client.post(reverse("expense-delete", args=[expense.id]))
    assert delete_resp.status_code == 302
    assert not Expense.objects.filter(id=expense.id).exists()


@pytest.mark.django_db
def test_expense_form_has_category_picker(auth_client):
    response = auth_client.get(reverse("expense-create"))
    content = response.content.decode()
    assert "category-picker" in content
    assert "category-card" in content


@pytest.mark.django_db
def test_income_crud(auth_client, user, user_income_category):
    create_resp = auth_client.post(
        reverse("income-create"),
        {
            "income_category": user_income_category.id,
            "amount": "5000.00",
            "received_at": date.today(),
            "comment": "Зарплата",
        },
    )
    assert create_resp.status_code == 302

    income = Income.objects.get(user=user)
    assert income.amount == Decimal("5000.00")


@pytest.mark.django_db
def test_user_cannot_edit_foreign_expense(auth_client, another_user):
    foreign_category = ExpenseCategory.objects.get(user=another_user, name="Транспорт")
    foreign_expense = Expense.objects.create(
        user=another_user,
        expense_category=foreign_category,
        amount=Decimal("50.00"),
        spent_at=date.today(),
    )

    response = auth_client.get(reverse("expense-update", args=[foreign_expense.id]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_statistics_page_default_month(auth_client):
    response = auth_client.get(reverse("statistics"))
    assert response.status_code == 200
    assert "category-chips" in response.content.decode()


@pytest.mark.django_db
def test_statistics_day_period(auth_client, user_expense_category):
    Expense.objects.create(
        user=user_expense_category.user,
        expense_category=user_expense_category,
        amount=Decimal("100.00"),
        spent_at=date(2026, 1, 15),
    )
    response = auth_client.get(
        reverse("statistics"),
        {"period": "day", "selected_date": "2026-01-15"},
    )
    assert response.status_code == 200
    assert "100" in response.content.decode()


@pytest.mark.django_db
def test_statistics_custom_period(auth_client):
    response = auth_client.get(
        reverse("statistics"),
        {
            "period": "custom",
            "start_date": "2026-01-01",
            "end_date": "2026-01-31",
        },
    )
    assert response.status_code == 200