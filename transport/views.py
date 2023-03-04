from django.shortcuts import render

# Create your views here.


def showLandingPage(request):
    return render(request, "transport/landingPage.html")


def showLoginPage(request):
    return render(request, "transport/loginPage.html")


def showLoginPageTruck(request):
    return render(request, "transport/loginPageTruck.html")


def showSignupPage(request):
    return render(request, "transport/signupPage.html")


def showSignupPageTruck(request):
    return render(request, "transport/signupPageTruck.html")


def showPaymentPage(request):
    return render(request, "transport/paymentPage.html")


def showBookingPage(request):
    return render(request, "transport/bookingPage.html")


def showDriversInterface(request):
    return render(request, "transport/driversInterface.html")
