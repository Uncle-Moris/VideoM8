from django.urls import path
from users.views import  logout_user, SuccessView, RegistrationView, LoginView

app_name = "users"

urlpatterns = [
    path('register', RegistrationView.as_view() , name='register'),
    path('login', LoginView.as_view() , name='login'),
    path('logout', logout_user, name='logout'),
    path('success', SuccessView.as_view(), name='success')
]