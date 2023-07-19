
from django.shortcuts import render , HttpResponse ,redirect
from bike.models import Person , Passenger, Driver, Notification
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login
import requests,json
from django.contrib import messages

import phonenumbers 





def home(request):
      return render(request, "home.html",{'nbar': 'h'})


def register(request):
      print("inside")
      if   request.method=="POST" :
            print("in")
            Phone=request.POST.get("uname")
            Name=request.POST.get("name")
            Password=request.POST.get("pwd")
            try :
                  pobj = phonenumbers.parse(Phone, None)
                  if (phonenumbers.is_possible_number(pobj) and phonenumbers.is_valid_number(pobj))==False:
                   messages.warning(request, "Oops phone number invalid ....please check the format  ")
                   return redirect("/register")
                  else:
                        print("VALID_PHONE" ,pobj , Phone)
                        print(phonenumbers.is_possible_number(pobj))
                        print(phonenumbers.is_valid_number(pobj))
           

                  #p=Person(UserName=Phone,Password=Password )
                  #p.save()
                  messages.success(request, "You have been successfully registered ! ")
                  User.objects.create_user(Phone, '', Password ,first_name=Name)
                  
            except phonenumbers.NumberParseException as e:
                   messages.warning(request, "Oops phone number invalid ....please check the format  ")
                   return redirect("/register")

            
            #return render(request, "login.html")
      return render(request, "login.html",{'nbar': 'l'})


def loginUser(request):
      print("in")
      UserName=request.POST.get("uname")
      Password=request.POST.get("pwd")
      print("reached")
      user = authenticate(username=UserName, password=Password)
      print(user)
      if user is not None:
            print("huun")
            if request.POST.get("role1")=="1":
                  print("driver huun")
                  login(request,user)
                  messages.success(request, "You have been successfully logged in ! ")
                  return redirect("/driver")
            
            elif request.POST.get("role1")=="2":
                  print("passenger huun")
                  login(request,user)
                  messages.success(request, "You have been successfully logged in ! ")
                  return redirect("/passenger")
      else:
            return render(request, "login.html",{'nbar': 'l'})

      

def logoutUser(request):
      logout(request)
      messages.success(request, "You have been successfully logged out ! ")
      return redirect("/register")
      pass



def driver(request):
      if request.user.is_anonymous:
             print("unlknown")
             return redirect("/register")
      if request.method=="POST":
            messages.success(request, "Your ride details have been shared with potential passengers. Please check Active Rides section below to view any matching rides")
            phone=request.user.username
            pwd=request.user.password
            name=request.user.first_name
            Source=request.POST.get("src")
            Destination=request.POST.get("dest")
            DateT=request.POST.get("datetime")
            srcres=requests.get("https://api.tomtom.com/search/2/geocode/"+str(Source)+".json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
            srcgeo=srcres.json()["results"][0]["position"]
            destres=requests.get("https://api.tomtom.com/search/2/geocode/"+str(Destination)+".json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
            destgeo=destres.json()["results"][0]["position"]
            slat,slon,dlat,dlon=srcgeo["lat"],srcgeo["lon"],destgeo["lat"],destgeo["lon"]
            psng = Passenger.objects.all()
            flag=0
            for p in psng:
                  usefuld,rest=str(p.RideDate).split("+")
                  if str(usefuld)==str(DateT)  and abs(float(p.SourceLat)-slat)<=0.0005  and abs(float(p.SourceLon)-slon)<=0.0005 and abs(float(p.DestinationLat)-dlat)<=0.0005  and abs(float(p.DestinationLon)-dlon)<=0.0005:
                        tbd=p.UserName
                        pname=p.First_Name
                        query={
                              "origins": [
                              {
                                    "point": { "latitude": slat, "longitude": slon }
                              }
                              ],
                              "destinations": [
                              {
                                    "point": { "latitude":dlat, "longitude": dlon}
                              }
                              ]
                              
                              }
                        print(query,"query")
                        h={"Content-Type":"application/json"}
                        response = requests.post('https://api.tomtom.com/routing/matrix/2?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv',json=query,headers=h)
                        distance=response.json()["data"][0][ "routeSummary"]["lengthInMeters"]/1000
                        fare=distance*10
                        print(fare,"fare")
                        Notice=Notification(Source=Source,Destination=Destination,Fare=fare,DateTime=DateT,Driver_Name=name,Passenger_Name=pname,Passenger_Phone=tbd,Driver_Phone=phone)
                        Notice.save()
                        Passenger.objects.filter(UserName=tbd).delete()
                        flag=1
                        
                  
            if flag==0:
                  d=Driver(UserName=phone,First_Name=name,Password=pwd,SourceLat=slat,SourceLon=slon,DestinationLat=dlat,DestinationLon=dlon,RideDate=DateT)
                  d.save()
                        

      notifications=list(Notification.objects.filter(Driver_Phone=request.user.username))
      if notifications!=[]:
            curr=notifications[0]
            context={"pk":curr.id,"RideTitle":curr.Source+" to "+curr.Destination,"Source":curr.Source,"Destination":curr.Destination,"Rider":curr.Driver_Name,"Passenger":curr.Passenger_Name,
            "Fare":curr.Fare,"dphone":curr.Driver_Phone , "pphone": curr.Passenger_Phone}
            #Driver.objects.filter(Username=tbd).delete()
            return render(request, "driver.html",context=context)
      else:
            return render(request, "driver.html")



def passenger(request):
      if request.user.is_anonymous:
             print("unlknown")
             return redirect("/register")
      distanceval=-1
      if request.method=="POST":
            messages.success(request, "Your request has been noted . Please check Active Rides section below to view any matching rides")
            phone=request.user.username
            pwd=request.user.password
            name=request.user.first_name
            Source=request.POST.get("src")
            Destination=request.POST.get("dest")
            DateT=request.POST.get("datetime")
            srcres=requests.get("https://api.tomtom.com/search/2/geocode/"+str(Source)+".json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
            srcgeo=srcres.json()["results"][0]["position"]
            destres=requests.get("https://api.tomtom.com/search/2/geocode/"+str(Destination)+".json?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv")
            destgeo=destres.json()["results"][0]["position"]
            slat,slon,dlat,dlon=srcgeo["lat"],srcgeo["lon"],destgeo["lat"],destgeo["lon"]
            Drivers = Driver.objects.all()
            flag=0
            for driver in Drivers:
                  usefuld,rest=str(driver.RideDate).split("+")
                  print(str(usefuld),str(DateT),"date")
                  if str(driver.RideDate)==str(DateT) and abs(float(driver.SourceLat)-slat)<=0.0005  and abs(float(driver.SourceLon)-slon)<=0.0005 and abs(float(driver.DestinationLat)-dlat)<=0.0005  and abs(float(driver.DestinationLon)-dlon)<=0.0005:
                        tbd=driver.UserName
                        dname=driver.First_Name
                        query={
                              "origins": [
                              {
                                    "point": { "latitude": slat, "longitude": slon }
                              }
                              ],
                              "destinations": [
                              {
                                    "point": { "latitude": dlat, "longitude": dlon}
                              }
                              ]
                              
                              }
                        print(query,"query")
                        h={"Content-Type":"application/json"}
                        response = requests.post('https://api.tomtom.com/routing/matrix/2?key=lfJylnZv8kZrCpdt3cVVCLD3HwnY3TQv',json=query,headers=h)
                        distance=response.json()["data"][0][ "routeSummary"]["lengthInMeters"]/1000
                        fare=distance*10
                        distanceval=distance
                        
                        Notice=Notification(Source=Source,Destination=Destination,Fare=fare,DateTime=DateT,Driver_Name=dname,Passenger_Name=name,Passenger_Phone=phone,Driver_Phone=tbd)
                        Notice.save()
                        Driver.objects.filter(UserName=tbd).delete()
                        flag=1
                        
            if flag==0:
                  p=Passenger(UserName=phone,First_Name=name ,Password=pwd,SourceLat=slat,SourceLon=slon,DestinationLat=dlat,DestinationLon=dlon,RideDate=DateT)
                  p.save()      

            

      notifications=list(Notification.objects.filter(Passenger_Phone=request.user.username))
      print(notifications)
      if notifications!=[]:
            curr=notifications[0]
            
            context={"d":distanceval,"pk":curr.id,"RideTitle":curr.Source," to ":curr.Destination,"Source":curr.Source,"Destination":curr.Destination,"Rider":curr.Driver_Name,"Passenger":curr.Passenger_Name,
            "Fare":curr.Fare ,"dphone":curr.Driver_Phone , "pphone": curr.Passenger_Phone}
            #Driver.objects.filter(Username=tbd).delete()
            return render(request, "passenger.html",context=context)
      else:
             return render(request, "passenger.html")



def rideover(request):
      if request.method=="POST":

            print("deleted")
            tobedel=int(request.POST.get("pk"))
            
            Notification.objects.filter(id=tobedel).delete()
            '''inst=Notification.objects.get(Fare=117)
            print(inst.id,"printing")
            inst.delete()'''
            return redirect("/passenger")
      

def contactus(request):
      return render(request,"contactus.html"  , {'nbar': 'c'})



def aboutus(request):
      return render(request,"aboutus.html",{'nbar': 'a'})
      
