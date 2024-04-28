from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('user_registration_view',views.UserRegistrationView.as_view(), name="user_registration_view"),
    path('user_registration', views.UserRegistration.as_view(), name='user_registration'),
    
]
