from decimal import Decimal

from django.db.models import F, Sum

from tracker.models import Expense, Income


def _chart_payload(rows) -> dict:
    labels = [row["category_name"] for row in rows]
    values = [float(row["total"]) for row in rows]
    return {
        "labels": labels,
        "values": values,
    }


def build_expense_statistics(user, start_date, end_date, category_ids=None):
    queryset = Expense.objects.filter(
        user=user,
        spent_at__range=(start_date, end_date),
    )
    if category_ids:
        queryset = queryset.filter(expense_category_id__in=category_ids)

    total = queryset.aggregate(total=Sum("amount")).get("total") or Decimal("0")
    breakdown_by_category = list(
        queryset.annotate(category_name=F("expense_category__name"))
        .values("category_name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    return {
        "total": total,
        "breakdown_by_category": breakdown_by_category,
        "top_categories": breakdown_by_category[:5],
        "chart": _chart_payload(breakdown_by_category),
    }


def build_income_statistics(user, start_date, end_date, category_ids=None):
    queryset = Income.objects.filter(
        user=user,
        received_at__range=(start_date, end_date),
    )
    if category_ids:
        queryset = queryset.filter(income_category_id__in=category_ids)

    total = queryset.aggregate(total=Sum("amount")).get("total") or Decimal("0")
    breakdown_by_category = list(
        queryset.annotate(category_name=F("income_category__name"))
        .values("category_name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    return {
        "total": total,
        "breakdown_by_category": breakdown_by_category,
        "top_categories": breakdown_by_category[:5],
        "chart": _chart_payload(breakdown_by_category),
    }