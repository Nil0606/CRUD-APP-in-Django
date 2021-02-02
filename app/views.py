from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from .models import student

# function for show and add student object

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        mobile=request.POST['mobile']
        student_exist=student.objects.filter(name=name)
        if not student_exist:
            new_student=student(name=name,age=age,mobile=mobile)
            new_student.save()
    context={}
    context['student_list']=student.objects.all()
    return render(request,'app/home.html',context)

# function for delete student object

def delete(request,id):
    stu=student.objects.get(pk=id)
    stu.delete()
    return HttpResponseRedirect(reverse("home"))

# function for update student object

def update(request,id):
    stu=student.objects.get(pk=id)
    update=stu
    stu.delete()
    context = {}
    context['student_list'] = student.objects.all()
    context['update']=update
    return render(request,'app/update.html',context)