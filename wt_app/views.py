from django.shortcuts import render

from .models import Wb
from .models import SB

def selectpage(request):
    return render(request,'registration/first.html',{})

def signuppage(request):
    return render(request,'registration/Patient.html',{})
    
def signuppage2(request):  
    return render(request,'registration/Doctor.html',{})



def docdashbord(request):
    
    inputtext1 = request.POST.get("first_Name")
    inputtext2 = request.POST.get("last_Name")
    inputtext3 = request.POST.get("img")
    inputtext4 = request.POST.get("username")
    inputtext5 = request.POST.get("Email_id")
    inputtext6 = request.POST.get("psw") 
    inputtext7 = request.POST.get("line_1")
    inputtext8 = request.POST.get("city")
    inputtext9 = request.POST.get("state")
    inputtext10 = request.POST.get("pincode")
    post = Wb(first_Name=inputtext1,last_Name=inputtext2,img=inputtext3,username=inputtext4,Email_id=inputtext5,psw=inputtext6,line_1=inputtext7,city=inputtext8,state=inputtext9,pincode=inputtext10)
    Wb.save(post)
    a = Wb.objects.all()    
    return render(request,"registration/ddashboard.html",{'a':a})
            

def patdashbord(request):
    inputtext11 = request.POST.get("first_Name1")
    inputtext22 = request.POST.get("last_Name1")
    inputtext33 = request.POST.get("img1")
    inputtext44 = request.POST.get("username1")
    inputtext55 = request.POST.get("Email_id1")
    inputtext66 = request.POST.get("psw1") 
    inputtext77 = request.POST.get("line_11")
    inputtext88 = request.POST.get("city1")
    inputtext99 = request.POST.get("state1")
    inputtext100 = request.POST.get("pincode1")
    post = SB(first_Name1=inputtext11,last_Name1=inputtext22,img1=inputtext33,username1=inputtext44,Email_id1=inputtext55,psw1=inputtext66,line_11=inputtext77,city1=inputtext88,state1=inputtext99,pincode1=inputtext100)
    SB.save(post)
    a = SB.objects.all()    
    
    return render(request,"registration/pdashboard.html",{"a":a})
                
