from django.shortcuts import render

# Create your views here.
def showLandingPage(request):
    return render(request,"transport/landingPage.html")