from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.sign_in),
    path('register_business', views.register_business),
    path('logout', views.logout),
    path('search', views.searchfood),
    path('business_profile/<int:businessuser_id>', views.business_profile),
    path('business_login', views.business_login),
    path('business_profile/update_business/<int:businessuser_id>', views.update_business),

]