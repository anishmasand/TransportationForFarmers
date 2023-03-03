from django.urls import path
from . import views

urlpatterns=[
    path('landingPage',views.showLandingPage,name="landingPage"),
    path('loginPage',views.showLoginPage,name="loginPage"),
    path('signupPage',views.showSignupPage,name="signupPage"),
    path('paymentPage',views.showPaymentPage,name="paymentPage"),
    path('bookingPage',views.showBookingPage,name="bookingPage"),
]