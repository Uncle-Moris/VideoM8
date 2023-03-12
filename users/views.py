from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView

def register_user(request):
    if request.method == "POST":
        pass




# Login
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('users:success')
            else:
                messages.error(request, "Invalid username or password.")


    form = AuthenticationForm()
    return render(request, 'users/user_login.html', {'form': form})


class LoginView(FormView):
    form_class = AuthenticationForm()
    template_name = 'users/user_login.html'
    success_url = reverse_lazy("users:success")





def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('users:success')


class SuccessView(TemplateView):
    template_name = "users/success.html"
