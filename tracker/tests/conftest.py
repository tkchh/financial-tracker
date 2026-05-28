import pytest
from django.contrib.auth.models import User
from django.test import Client

from tracker.models import ExpenseCategory, IncomeCategory
from tracker.services import (
    create_default_expense_categories,
    create_default_income_categories,
)


def _setup_user(username: str) -> User:
    account = User.objects.create_user(username=username, password="pass12345")
    create_default_expense_categories(account)
    create_default_income_categories(account)
    return account


@pytest.fixture
def user(db):
    return _setup_user("user1")


@pytest.fixture
def another_user(db):
    return _setup_user("user2")


@pytest.fixture
def auth_client(user):
    client = Client()
    client.login(username="user1", password="pass12345")
    return client


@pytest.fixture
def user_expense_category(user):
    return ExpenseCategory.objects.get(user=user, name="Продукты")


@pytest.fixture
def user_income_category(user):
    return IncomeCategory.objects.get(user=user, name="Зарплата")