from django.db import transaction

from tracker.models import ExpenseCategory, IncomeCategory

DEFAULT_EXPENSE_CATEGORIES = (
    "Дом",
    "Продукты",
    "Транспорт",
    "Здоровье",
    "Еда вне дома",
    "Развлечения",
    "Красота",
    "Образование",
    "Домашние животные",
)

DEFAULT_INCOME_CATEGORIES = (
    "Зарплата",
    "Стипендия",
    "Переводы",
)


@transaction.atomic
def create_default_expense_categories(user) -> None:
    existing = set(
        ExpenseCategory.objects.filter(user=user).values_list("name", flat=True)
    )
    to_create = [
        ExpenseCategory(user=user, name=name, is_default=True)
        for name in DEFAULT_EXPENSE_CATEGORIES
        if name not in existing
    ]
    if to_create:
        ExpenseCategory.objects.bulk_create(to_create)


@transaction.atomic
def create_default_income_categories(user) -> None:
    existing = set(
        IncomeCategory.objects.filter(user=user).values_list("name", flat=True)
    )
    to_create = [
        IncomeCategory(user=user, name=name, is_default=True)
        for name in DEFAULT_INCOME_CATEGORIES
        if name not in existing
    ]
    if to_create:
        IncomeCategory.objects.bulk_create(to_create)