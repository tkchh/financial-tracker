from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from tracker.forms import SignUpForm
from tracker.services import (
    create_default_expense_categories,
    create_default_income_categories,
)


class HomeView(TemplateView):
    template_name = "tracker/home.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("expense-list")
        return super().get(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = "registration/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("expense-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        create_default_expense_categories(self.object)
        create_default_income_categories(self.object)
        login(self.request, self.object)
        return response