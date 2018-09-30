from teachersapp1.models import Teachers


def teacher_list(request):
    teachers=Teachers.objects.all()
    context={"teacher_list":teachers}
    return render(request,'teacher.html',context)
