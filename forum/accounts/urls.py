from django.urls import path
from accounts.views import RegisterView, profile_view
from django.contrib.auth.views import LoginView, LogoutView
app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('userroom/', profile_view, name='room'),
]