from django.urls import path
from app_users import views
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.UserView.as_view(), name='me'),
]