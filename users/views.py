from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/user_registration.html'
    success_url = reverse_lazy('video-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'users/user_login.html'
    success_url = reverse_lazy("users:success")

    def form_valid(self, form):
        request = self.request
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return super().form_valid(form)
        else:
            messages.error(request, "Invalid username or password.")
            return self.form_invalid(form)


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('video-list')


class SuccessView(TemplateView):
    template_name = "users/success.html"
