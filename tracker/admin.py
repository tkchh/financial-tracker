from django.contrib import admin

from tracker.models import Expense, ExpenseCategory, Income, IncomeCategory


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "is_default")
    list_filter = ("is_default",)
    search_fields = ("name", "user__username")


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "is_default")
    list_filter = ("is_default",)
    search_fields = ("name", "user__username")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "expense_category", "amount", "spent_at")
    list_filter = ("spent_at", "expense_category")
    search_fields = ("user__username", "comment")


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "income_category", "amount", "received_at")
    list_filter = ("received_at", "income_category")
    search_fields = ("user__username", "comment")