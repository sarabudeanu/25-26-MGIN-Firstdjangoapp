from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from patientmanagerapp.models import Patient

# Create your views here.

def helloworld_view(request: HttpRequest):
    return HttpResponse("Hello World")


def add_patient(request: HttpRequest):

    # todo: Check SVNR
    isSVNRValid = True

    if (request.method == "POST"):

        #print()
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

    if request.method == "POST":
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