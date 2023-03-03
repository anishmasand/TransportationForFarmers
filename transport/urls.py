from django.urls import path, include
from . import views

urlpatterns = [
    path('landingPage', views.showLandingPage, name="landingPage"),
    path('loginPage', views.showLoginPageTruck, name="loginPage"),
    path('loginPageTruck', views.showLoginPageTruck, name="loginPageTruck"),
    path('signupPageTruck', views.showSignupPageTruck, name="signupPageTruck"),
    path('signupPage', views.showSignupPage, name="signupPage"),
    path('paymentPage', views.showPaymentPage, name="paymentPage"),
    path('bookingPage', views.showBookingPage, name="bookingPage"),
    path('bookingPage', views.showBookingPage, name="bookingPage"),
    path('registerFarmer', views.registerFarmer, name="registerFarmer"),
    path('authenticateFarmer', views.authenticateFarmer, name="authenticateFarmer"),
    path('registerDriver', views.registerDriver, name="registerDriver"),
    path('authenticateDriver', views.authenticateDriver, name="authenticateDriver"),
]