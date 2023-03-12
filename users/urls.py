from django.urls import path
from users.views import register_user, login_user, logout_user, SuccessView

app_name = "users"

urlpatterns = [
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('success', SuccessView.as_view(), name='success')
]