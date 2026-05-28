from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib import messages

from tracker.forms import ExpenseCategoryForm, IncomeCategoryForm
from tracker.models import ExpenseCategory, IncomeCategory
from tracker.views.mixins import UserOwnedQuerySetMixin


class ExpenseCategoryListView(LoginRequiredMixin, UserOwnedQuerySetMixin, ListView):
    model = ExpenseCategory
    template_name = "tracker/expense_category_list.html"


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("expense-category-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseCategoryUpdateView(LoginRequiredMixin, UserOwnedQuerySetMixin, UpdateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("expense-category-list")


class ExpenseCategoryDeleteView(LoginRequiredMixin, UserOwnedQuerySetMixin, DeleteView):
    model = ExpenseCategory
    template_name = "tracker/confirm_delete.html"
    success_url = reverse_lazy("expense-category-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Нельзя удалить категорию: есть связанные расходы."
            )
            return redirect(self.success_url)


class IncomeCategoryListView(LoginRequiredMixin, UserOwnedQuerySetMixin, ListView):
    model = IncomeCategory
    template_name = "tracker/income_category_list.html"


class IncomeCategoryCreateView(LoginRequiredMixin, CreateView):
    model = IncomeCategory
    form_class = IncomeCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("income-category-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeCategoryUpdateView(LoginRequiredMixin, UserOwnedQuerySetMixin, UpdateView):
    model = IncomeCategory
    form_class = IncomeCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("income-category-list")


class IncomeCategoryDeleteView(LoginRequiredMixin, UserOwnedQuerySetMixin, DeleteView):
    model = IncomeCategory
    template_name = "tracker/confirm_delete.html"
    success_url = reverse_lazy("income-category-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Нельзя удалить категорию: есть связанные доходы."
            )
            return redirect(self.success_url)