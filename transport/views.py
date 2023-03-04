from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from transport.models import Farmer,Driver

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

def registerFarmer(request):
    fullname=request.POST['fullname']
    email=request.POST['email']
    password=request.POST['password']
    mobile=request.POST['mobile']
    location=request.POST['location']
    supply_capacity=request.POST['supply_capacity']
    #hashed password
    # hashed_password=make_password(password)
    farmer=Farmer(name=fullname,email=email,password=password,mobile=mobile,location=location,supply_capacity=supply_capacity)
    farmer.save()
    return render(request,'transport/loginPage.html')

def authenticate(request):
    # print("helloo")
    email=request.POST['email']
    password=request.POST['password']
    response=Farmer.objects.filter(email=email,password=password)
    print(response)
    if(response):
        return render(request,"transport/bookingPage.html")
    print("failed")
    return render(request,"transport/errorPage.html")

def registerDriver(request):
    print("hello")
    fullname=request.POST['fullname']
    email=request.POST['email']
    password=request.POST['password']
    mobile=request.POST['mobile']
    rating=request.POST['rating']
    license=request.POST['license']
    #hashed password
    # hashed_password=make_password(password)
    driver=Driver(name=fullname,email=email,password=password,mobile=mobile,rating=rating,rides_made=0,license_no=license)
    driver.save()
    return render(request,'transport/loginPageTruck.html')

def authenticateDriver(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    response=Driver.objects.filter(email=email,password=password)
    if(response):
        return render(request,"transport/bookingPage.html")
    return render(request,"transport/errorPage.html")
