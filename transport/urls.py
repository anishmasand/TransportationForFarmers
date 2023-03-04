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
    path('driversInterface', views.showDriversInterface, name="driversInterface"),
    # path('accounts/', include('allauth.urls')),
]
