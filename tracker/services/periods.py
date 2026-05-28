from calendar import monthrange
from datetime import date


def get_current_month_range(today: date | None = None) -> tuple[date, date]:
    current_day = today or date.today()
    return get_month_range(current_day.year, current_day.month)


def get_month_range(year: int, month: int) -> tuple[date, date]:
    last_day = monthrange(year, month)[1]
    return date(year, month, 1), date(year, month, last_day)