from django.shortcuts import render,redirect
from .import views
from studentapp.models import StudentTable

# Create your views here.
def f4(request):
    return render(request,'student.html')
def details(request):
    if request.method=='POST':
        s_name=request.POST['s_name']
        add=request.POST['add']
        age=request.POST['age']
        email=request.POST['email']
        join=request.POST['jd']
        gend=request.POST['gen']
        quali=request.POST['quali']
        mob=request.POST['mob']
        student=StudentTable(student_name=s_name,address=add,age=age,email=email,joiningdate=join,gender=gend,qualifiation=quali,mobileno=mob)
        student.save()
        return redirect('/')
def show(request):
    student1=StudentTable.objects.all() 
    return render(request,'show.html',{'a':student1})  
def showdetails(request,pk):
    student1=StudentTable.objects.get(id=pk)
    return render(request,'showdetails.html',{'a':student1})
def editpage(request,pk):
    student2=StudentTable.objects.get(id=pk)
    qualification=StudentTable.objects.values('qualifiation').distinct 
    return render(request,'edit.html',{'s':student2,'q':qualification})
def edit_details(request,pk):
    if request.method=='POST':
        student2=StudentTable.objects.get(id=pk)
        student2.student_name=request.POST('s_name')
        student2.address=request.POST('add')
        student2.age=request.POST('age')
        student2.email=request.POST('email')
        student2.joiningdate=request.POST('jd')
        student2.gender=request.POST('gen')
        student2.qualifiation=request.POST('quali')
        student2.mobileno=request.POST('mob')
        student2.save()
        return redirect('show')
    return render(request,'edit.html')
def deletepage(request,pk):
    student2=StudentTable.objects.get(id=pk)
    student2.delete()
    return redirect('show')