from django.urls import path, include
from . import views

urlpatterns = [
    path('landingPage', views.showLandingPage, name="landingPage"),
    path('loginPage', views.showLoginPage, name="loginPage"),
    path('loginPageTruck', views.showLoginPageTruck, name="loginPageTruck"),
    path('signupPageTruck', views.showSignupPageTruck, name="signupPageTruck"),
    path('signupPage', views.showSignupPage, name="signupPage"),
    path('paymentPage', views.showPaymentPage, name="paymentPage"),
    path('bookingPage', views.showBookingPage, name="bookingPage"),
<<<<<<< HEAD
    path('driversInterface', views.showDriversInterface, name="driversInterface"),
    # path('accounts/', include('allauth.urls')),
]
=======
    path('bookingPage', views.showBookingPage, name="bookingPage"),
    path('registerFarmer', views.registerFarmer, name="registerFarmer"),
    path('authenticate', views.authenticate , name="authenticate"),
    path('registerDriver', views.registerDriver, name="registerDriver"),
    path('authenticateDriver', views.authenticateDriver, name="authenticateDriver"),
]
>>>>>>> 4b75e2e29510409485bf80811c3e11861371a95f
