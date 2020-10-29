from django.shortcuts import render,HttpResponse
from crudapp.models import EmpModel
from django.contrib import messages
from crudapp.forms import Empforms
def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{"data":showall})

def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('id') and request.POST.get('empname') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('empsal') and request.POST.get('gender') and request.POST.get('address'):
            saverecord=EmpModel()
            saverecord.id = request.POST.get('id')
            saverecord.empname=request.POST.get('empname')
            saverecord.email = request.POST.get('email')
            saverecord.occupation = request.POST.get('occupation')
            saverecord.empsal = request.POST.get('empsal')
            saverecord.gender  = request.POST.get('gender')
            saverecord.address = request.POST.get('address')
            saverecord.save()
            messages.success(request,'HEY'+saverecord.empname+ 'IS SAVED SUCCESSFULLY..!')
            return render(request,'Insert.html')
        else:
            messages.success(request,'Not Done')
    else:
            return render(request,'Insert.html')

def Editemp(request,id):
    editempobj=EmpModel.objects.get(id=id)
    return render(request,'Edit.html',{"EmpModel":editempobj})

def updateemp(request,id):
     updateemp=EmpModel.objects.get(id=id)
     form=Empforms(request.POST,instance=updateemp)
     if form.is_valid():
         form.save()
         messages.success(request,"RECORD UPDATED SUCCESSFULLY..!!")
         return render(request,'Edit.html',{"EmpModel":updateemp})


def Delemp(request,id):
    delemployee=EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request,"Index.html",{"EmpModel":showdata})

def search(request):
    findbyname = request.GET['findbyname']
    show = EmpModel.objects.filter(empname__icontains=findbyname)
    return render(request, 'search.html', {"data": show})

def Multiplesearchemp(request):
    if request.method=="POST":
        gender=request.POST.get('gender')
        occupation = request.POST.get('occupation')
        empsearchobj=EmpModel.objects.raw('select * from employee where gender=%s and occupation=%s',[gender,occupation])
        return  render(request,'search.html',{'data1':empsearchobj})

def sortemp(request):
        empsortobj=EmpModel.objects.raw('select * from employee order by empname')
        return  render(request,'index.html',{'data':empsortobj})


def sortsal(request):
    empsortsalobj = EmpModel.objects.raw('select * from employee order by empsal')
    return render(request, 'index.html', {'data': empsortsalobj})

def refresh(request):
    refreshobj = EmpModel.objects.raw('select * from employee order by id')
    return render(request, 'index.html', {'data': refreshobj})
