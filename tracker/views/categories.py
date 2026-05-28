from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tracker.forms import ExpenseCategoryForm, IncomeCategoryForm
from tracker.models import ExpenseCategory, IncomeCategory


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "tracker/expense_category_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("expense-category-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("expense-category-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ExpenseCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ExpenseCategory
    template_name = "tracker/confirm_delete.html"
    success_url = reverse_lazy("expense-category-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            return redirect("expense-category-list")


class IncomeCategoryListView(LoginRequiredMixin, ListView):
    model = IncomeCategory
    template_name = "tracker/income_category_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class IncomeCategoryCreateView(LoginRequiredMixin, CreateView):
    model = IncomeCategory
    form_class = IncomeCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("income-category-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = IncomeCategory
    form_class = IncomeCategoryForm
    template_name = "tracker/category_form.html"
    success_url = reverse_lazy("income-category-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class IncomeCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = IncomeCategory
    template_name = "tracker/confirm_delete.html"
    success_url = reverse_lazy("income-category-list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            return redirect("income-category-list")