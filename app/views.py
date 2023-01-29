from django.shortcuts import render
from app.models import *
# Create your views here.
def home(request):
    return render(request,"home.html")

def all_students(request):
    data=Student_marks.objects.all()
    new_data=[]
    for i in data:
        k=((int(i.maths) + int(i.physics) + int(i.chemistry) + int(i.english) + int(i.biology) + int(i.economics) + int(i.history) + int(i.civics))/8 )
        i.maths=k
    d={"data":data,"new_data":new_data}
    return render(request,"all_students.html",d)

def students_marks_above(request):
    data=Student_marks.objects.all()
    d={"data":data}
    if request.method=="POST":
        percentage=int(request.POST["percentage"])
        new_data=[]
        for i in data:
            k=((int(i.maths) + int(i.physics) + int(i.chemistry) + int(i.english) + int(i.biology) + int(i.economics) + int(i.history) + int(i.civics))/8 )
            if k>=percentage:
                new_data.append(i)
        d={"data":new_data,"percentage":percentage}
        return render(request,"display_percentage.html",d)
    return render(request,"students_marks_above.html")

def students_genderwise(request):
    data=Student_marks.objects.all()
    if request.method=="POST":
        gen=request.POST["gender"]
        new_data=[]
        for i in data:
            if i.gender.upper()==gen.upper():
                new_data.append(i)
        d={"data":new_data,"gen":gen}
        return render(request,"display_percentage.html",d)
    return render(request,"students_genderwise.html")

def specific_name(request):
    data=Student_marks.objects.all()
    if request.method=="POST":
        sp_name=request.POST["sp_name"]
        new_data=[]
        for i in data:
            if i.name.lower().count(sp_name.lower())>0:
                new_data.append(i)
        d={"data":new_data}
        return render(request,"display_percentage.html",d)
    return render(request,"specific_name.html")

def all_cutoff(request):
    data=Student_marks.objects.all()
    if request.method=="POST":
        k=request.POST["cut"]
        new_data=[]
        for i in data:
            if i.maths>=int(k):
                if i.chemistry>=int(k):
                    if i.physics>=int(k):
                        if i.english>=int(k):
                            if i.biology>=int(k):
                                if i.history>=int(k):
                                    if i.civics>=int(k):
                                        if i.economics>=int(k):
                                            new_data.append(i)
        d={"data":new_data}
        return render(request,"display_percentage.html",d)
    return render(request,"all_cutoff.html")
