from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_attempt, name="login"),
    path('otp/', views.check_otp, name="otp"),
    path('logout/', views.user_logout, name="logout"),
    path('userprofile/<uuid:pk>/', views.UserProfile.as_view(), name="user-profile"),
    path('joingroup/', views.JoinGroup.as_view(), name="join-group"),
    


]
