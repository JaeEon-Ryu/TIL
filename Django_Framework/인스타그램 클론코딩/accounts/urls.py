from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup

app_name = "accounts"

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'),name = 'login'),
    path('logout/',LogoutView.as_view(template_name = 'accounts/logout.html'),name = 'logout'),
]