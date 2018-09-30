from django.shortcuts import render

# Create your views here.
from teachersapp1.models import Teachers

def teacher_list(request):
    teachers=Teachers.objects.all()
    context={"teacher_list":teachers}
    return render(request,'teacher.html',context)

def teacher_details(request,code):
    teacher=Teachers.objects.get(code=code)
    context={"teacher":teacher}
    return render(request,'teacher.html',context)

