from django.urls import path
from django.contrib.auth import views as authViews
from . import views as userViews

from . import views


urlpatterns = [
    path('registration/', userViews.RegistrationView.as_view()),
    path('login/', authViews.LoginView.as_view(), name='login'),
    path('exit/', authViews.LogoutView.as_view(), name='exit')
]