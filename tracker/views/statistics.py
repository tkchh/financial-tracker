from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from tracker.forms import StatisticsFilterForm
from tracker.selectors import build_expense_statistics, build_income_statistics
from tracker.services import calculate_balance


class StatisticsView(LoginRequiredMixin, TemplateView):
    template_name = "tracker/statistics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.copy() if self.request.GET else None
        if not query:
            today = date.today()
            query = {
                "period": "month",
                "selected_month": today.strftime("%Y-%m"),
            }
        form = StatisticsFilterForm(query, user=self.request.user)

        expense_stats = None
        income_stats = None
        balance = None

        if form.is_valid() and form.cleaned_data.get("start_date"):
            start = form.cleaned_data["start_date"]
            end = form.cleaned_data["end_date"]
            expense_categories = form.cleaned_data.get("expense_categories")
            income_categories = form.cleaned_data.get("income_categories")

            expense_stats = build_expense_statistics(
                self.request.user,
                start,
                end,
                category_ids=(
                    list(expense_categories.values_list("id", flat=True))
                    if expense_categories
                    else None
                ),
            )
            income_stats = build_income_statistics(
                self.request.user,
                start,
                end,
                category_ids=(
                    list(income_categories.values_list("id", flat=True))
                    if income_categories
                    else None
                ),
            )
            balance = calculate_balance(self.request.user, start, end)

        context["form"] = form
        context["expense_stats"] = expense_stats
        context["income_stats"] = income_stats
        context["balance"] = balance
        context["period"] = (
            form.cleaned_data.get("period") if form.is_valid() else "month"
        )
        return context