from django.urls import path
from .views import register, SignUp
from django.contrib.auth import views as authViews

urlpatterns = [
    path('register/', register, name='register'),
    path('signup/', SignUp.as_view() , name='signup'),
    path('logout', authViews.LogoutView.as_view(), name='logout')
    
]