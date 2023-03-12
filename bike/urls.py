from django.contrib import admin
from django.urls import path
from bike import views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home , name="homepage"),
     path('register/', views.register , name="registerpage"),
      path('login/', views.loginUser , name="loginpage"),
      path('logout/', views.logoutUser , name="logoutpage"),
     path('passenger/', views.passenger , name="passengerpage"),
     path('driver/', views.driver , name="driverpage"),
     path('rideover/', views.rideover , name="rideover"),
     path('contactus/', views.contactus , name="contactus"),
     path('aboutus/', views.aboutus , name="aboutus")
]