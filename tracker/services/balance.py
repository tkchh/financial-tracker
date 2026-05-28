from datetime import date
from decimal import Decimal

from django.db.models import Sum

from tracker.models import Expense, Income


def get_expense_total_for_period(user, start_date: date, end_date: date) -> Decimal:
    return (
        Expense.objects.filter(user=user, spent_at__range=(start_date, end_date))
        .aggregate(total=Sum("amount"))
        .get("total")
        or Decimal("0")
    )


def get_income_total_for_period(user, start_date: date, end_date: date) -> Decimal:
    return (
        Income.objects.filter(user=user, received_at__range=(start_date, end_date))
        .aggregate(total=Sum("amount"))
        .get("total")
        or Decimal("0")
    )


def calculate_balance(user, start_date: date, end_date: date) -> dict:
    total_income = get_income_total_for_period(user, start_date, end_date)
    total_expense = get_expense_total_for_period(user, start_date, end_date)
    balance = total_income - total_expense
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "start_date": start_date,
        "end_date": end_date,
    }