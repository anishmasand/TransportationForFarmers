from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password

from transport.models import Farmer



# Create your views here.
def showLandingPage(request):
    return render(request,"transport/landingPage.html")
def showLoginPage(request):
    return render(request,"transport/loginPage.html")
def showSignupPage(request):
    return render(request,"transport/signupPage.html")
def showPaymentPage(request):
    return render(request,"transport/paymentPage.html")
def showBookingPage(request):
    return render(request,"transport/bookingPage.html")
def registerFarmer(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    mobile=request.POST['mobile']
    location=request.POST['location']
    supply_capacity=request.POST['supply_capacity']
    hashed_password=make_password(password)
    farmer=Farmer(name=name,email=email,password=hashed_password,mobile=mobile,location=location,supply_capacity=supply_capacity)
    farmer.save()
def authenticate(request):
    email=request.POST['email']
    password=request.POST['password']
    response=Farmer.objects.get(email=email)
    if(response):
        if(check_password(password,response.password)):
            return render(request,"transport/bookingPage.html")
    return render(request,"transport/errorPage.html")
        
    
