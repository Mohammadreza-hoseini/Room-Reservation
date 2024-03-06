from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_attempt, name="login"),
    path('otp/', views.check_otp, name="otp"),
    path('logout/', views.user_logout, name="logout"),
]
