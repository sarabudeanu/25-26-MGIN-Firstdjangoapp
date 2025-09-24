from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from patientmanagerapp.models import Patient
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AbstractUser

# Create your views here.

def helloworld_view(request: HttpRequest):
    return HttpResponse("Hello World")


def add_patient(request: HttpRequest):
    #TODO Check if user is logged in
    print(f"is user authenticated: {request.user.is_active}")
    print(f"is user a staff member: {request.user.is_staff}")


    #TODO Check SVNR
    isSVNRValid = True

    if request.method == "POST" and request.user.is_staff:

        Patient.objects.create(
            first_name = request.POST.get("firstname"),
            last_name = request.POST["lastname"],
            birthday=request.POST.get("birthday"),
            svnr = request.POST["svnr"]
        )
        print(request.POST)
        
        return redirect("/patients/")
        

    return render(request, "addpatient.html", context={"isSVNRValid":isSVNRValid})


def list_patients(request:HttpRequest):

    return render(request, "listpatients.html", context={"patients":Patient.objects.all()})

def edit_patient(request: HttpRequest,id:int):

    if request.method == "POST" and request.user.is_staff:
        Patient.objects.filter(id=id).update(
            first_name=request.POST["firstname"],
            last_name=request.POST["lastname"],
            birthday=request.POST["birthday"],
            svnr=request.POST.get("svnr")
        )

        return redirect("/patients/")
    
    targetPatient = Patient.objects.get(id=id) # id von models = id aus parameter

    return render(request,"addpatient.html",context={"patient":targetPatient})

def delete_patient(request: HttpRequest,id:int):

    Patient.objects.filter(id=id).delete()

    return render(request,"listpatients.html",context={"patients":Patient.objects.all()})

def perform_login(request:HttpRequest):

    login_status = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user : AbstractUser | None = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            login_status = "SUCCESSFULL"
        else:
            #user is None
            login_status = "FAILED"


    return render(request,"login.html", context={"login_status":login_status})

def perform_logout(request:HttpRequest):
    logout(request)
    return redirect("/login/")