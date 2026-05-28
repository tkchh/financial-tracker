from django import forms

from tracker.models import Expense, ExpenseCategory, Income, IncomeCategory


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("expense_category", "amount", "spent_at", "comment")
        widgets = {
            "spent_at": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self._user = user
        self.fields["expense_category"].queryset = ExpenseCategory.objects.filter(
            user=user
        )
        self.fields["expense_category"].label = "Категория расхода"
        self.fields["expense_category"].widget = forms.RadioSelect()
        self.fields["expense_category"].empty_label = None

    def clean_expense_category(self):
        category = self.cleaned_data["expense_category"]
        if category.user != self._user:
            raise forms.ValidationError("Выберите категорию из своего списка.")
        return category


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ("income_category", "amount", "received_at", "comment")
        widgets = {
            "received_at": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self._user = user
        self.fields["income_category"].queryset = IncomeCategory.objects.filter(
            user=user
        )
        self.fields["income_category"].label = "Категория дохода"
        self.fields["income_category"].widget = forms.RadioSelect()
        self.fields["income_category"].empty_label = None

    def clean_income_category(self):
        category = self.cleaned_data["income_category"]
        if category.user != self._user:
            raise forms.ValidationError("Выберите категорию из своего списка.")
        return category