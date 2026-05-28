from django import forms

from tracker.models import ExpenseCategory, IncomeCategory
from tracker.services import get_month_range


class StatisticsFilterForm(forms.Form):
    PERIOD_CHOICES = (
        ("day", "День"),
        ("month", "Месяц"),
        ("custom", "Произвольный"),
    )

    period = forms.ChoiceField(choices=PERIOD_CHOICES, initial="month")
    selected_date = forms.DateField(
        required=False,
        label="Дата",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    selected_month = forms.CharField(
        required=False,
        label="Месяц",
        widget=forms.TextInput(attrs={"type": "month"}),
    )
    start_date = forms.DateField(
        required=False,
        label="Дата начала",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = forms.DateField(
        required=False,
        label="Дата окончания",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    expense_categories = forms.ModelMultipleChoiceField(
        required=False,
        label="Категории расходов",
        queryset=ExpenseCategory.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
    )
    income_categories = forms.ModelMultipleChoiceField(
        required=False,
        label="Категории доходов",
        queryset=IncomeCategory.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["expense_categories"].queryset = ExpenseCategory.objects.filter(
            user=user
        )
        self.fields["income_categories"].queryset = IncomeCategory.objects.filter(
            user=user
        )

    def clean(self):
        cleaned_data = super().clean()
        period = cleaned_data.get("period")

        if period == "day":
            selected_date = cleaned_data.get("selected_date")
            if not selected_date:
                self.add_error("selected_date", "Выберите день.")
                return cleaned_data
            cleaned_data["start_date"] = selected_date
            cleaned_data["end_date"] = selected_date

        elif period == "month":
            selected_month = cleaned_data.get("selected_month")
            if not selected_month:
                self.add_error("selected_month", "Выберите месяц.")
                return cleaned_data
            try:
                year_str, month_str = selected_month.split("-")
                year, month = int(year_str), int(month_str)
                if month < 1 or month > 12:
                    raise ValueError
            except ValueError:
                self.add_error("selected_month", "Некорректный месяц.")
                return cleaned_data
            start, end = get_month_range(year, month)
            cleaned_data["start_date"] = start
            cleaned_data["end_date"] = end

        elif period == "custom":
            if not cleaned_data.get("start_date") or not cleaned_data.get("end_date"):
                raise forms.ValidationError(
                    "Для произвольного периода укажите дату начала и окончания."
                )

        if (
            cleaned_data.get("start_date")
            and cleaned_data.get("end_date")
            and cleaned_data["start_date"] > cleaned_data["end_date"]
        ):
            raise forms.ValidationError("Дата начала не может быть больше даты конца.")

        return cleaned_data