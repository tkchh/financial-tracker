from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tracker.forms import ExpenseForm, IncomeForm
from tracker.models import Expense, Income
from tracker.services import calculate_balance, get_current_month_range


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = "tracker/expense_list.html"
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start, end = get_current_month_range()
        context["balance"] = calculate_balance(self.request.user, start, end)
        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "tracker/transaction_form.html"
    success_url = reverse_lazy("expense-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Новый расход"
        context["picker_variant"] = "expense"
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "tracker/transaction_form.html"
    success_url = reverse_lazy("expense-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Редактирование расхода"
        context["picker_variant"] = "expense"
        return context


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "tracker/confirm_delete.html"
    success_url = reverse_lazy("expense-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = "tracker/income_list.html"
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start, end = get_current_month_range()
        context["balance"] = calculate_balance(self.request.user, start, end)
        return context


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = "tracker/transaction_form.html"
    success_url = reverse_lazy("income-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Новый доход"
        context["picker_variant"] = "income"
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "tracker/transaction_form.html"
    success_url = reverse_lazy("income-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Редактирование дохода"
        context["picker_variant"] = "income"
        return context


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = "tracker/confirm_delete.html"
    success_url = reverse_lazy("income-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)