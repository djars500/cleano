from django.urls import path
from .views import main,myAppView, updateStatusRequest

urlpatterns = [

    path('', main, name='main'),
    path('myapps/', myAppView, name='myapps'),
    path('status-update/<int:pk>', updateStatusRequest, name="request_status_update")

]