from django.urls import path

from tracker.views import (
    ExpenseCategoryCreateView,
    ExpenseCategoryDeleteView,
    ExpenseCategoryListView,
    ExpenseCategoryUpdateView,
    ExpenseCreateView,
    ExpenseDeleteView,
    ExpenseListView,
    ExpenseUpdateView,
    HomeView,
    IncomeCategoryCreateView,
    IncomeCategoryDeleteView,
    IncomeCategoryListView,
    IncomeCategoryUpdateView,
    IncomeCreateView,
    IncomeDeleteView,
    IncomeListView,
    IncomeUpdateView,
    SignUpView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "expense-categories/",
        ExpenseCategoryListView.as_view(),
        name="expense-category-list",
    ),
    path(
        "expense-categories/new/",
        ExpenseCategoryCreateView.as_view(),
        name="expense-category-create",
    ),
    path(
        "expense-categories/<int:pk>/edit/",
        ExpenseCategoryUpdateView.as_view(),
        name="expense-category-update",
    ),
    path(
        "expense-categories/<int:pk>/delete/",
        ExpenseCategoryDeleteView.as_view(),
        name="expense-category-delete",
    ),
    path(
        "income-categories/",
        IncomeCategoryListView.as_view(),
        name="income-category-list",
    ),
    path(
        "income-categories/new/",
        IncomeCategoryCreateView.as_view(),
        name="income-category-create",
    ),
    path(
        "income-categories/<int:pk>/edit/",
        IncomeCategoryUpdateView.as_view(),
        name="income-category-update",
    ),
    path(
        "income-categories/<int:pk>/delete/",
        IncomeCategoryDeleteView.as_view(),
        name="income-category-delete",
    ),
    path("expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("expenses/new/", ExpenseCreateView.as_view(), name="expense-create"),
    path(
        "expenses/<int:pk>/edit/",
        ExpenseUpdateView.as_view(),
        name="expense-update",
    ),
    path(
        "expenses/<int:pk>/delete/",
        ExpenseDeleteView.as_view(),
        name="expense-delete",
    ),
    path("incomes/", IncomeListView.as_view(), name="income-list"),
    path("incomes/new/", IncomeCreateView.as_view(), name="income-create"),
    path(
        "incomes/<int:pk>/edit/",
        IncomeUpdateView.as_view(),
        name="income-update",
    ),
    path(
        "incomes/<int:pk>/delete/",
        IncomeDeleteView.as_view(),
        name="income-delete",
    ),
]