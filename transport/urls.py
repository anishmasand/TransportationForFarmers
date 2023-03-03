from django.urls import path
from . import views

urlpatterns=[
    path('landingPage',views.showLandingPage,name="landingPage"),
    # path('loginPage',views.showLoginPage,name="loginPage")
]