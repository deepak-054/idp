import django
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Timetable
from django.db.models import Q
import pandas as pd


def home(request):
    if request.method=='POST':
        slot1=request.POST.get('slot_1')
        slot2=request.POST.get('slot_2')
        day=request.POST.get('day')
        return redirect('slot_details',pk=slot1,qk=slot2,rk=day)
    return render(request, 'index.html')
def slotDetails(request,pk,qk,rk):
    login_data = request.POST.dict()
    start = pk
    end = qk
    day= rk
    s="slot"+start
    e="slot"+end
    teacher = Timetable.objects.filter(day=day)
    if(start=='1' or end =='1' ):
        teacher=teacher.filter(slot1=0)
    if(start=='2' or end =='2' ):
        teacher=teacher.filter(slot2=0)
    if(start=='3' or end =='3' ):
        teacher=teacher.filter(slot3=0)
    if(start=='4' or end =='4' ):
        teacher=teacher.filter(slot4=0)
    if(start=='5' or end =='5'):
        teacher=teacher.filter(slot5=0)
    if(start=='6' or end =='6'):
        teacher=teacher.filter(slot6=0)
    if(start=='7' or end =='7' ):
        teacher=teacher.filter(slot7=0)
    print(teacher)
    return render(request, 'slotDetails.html',context={'slot1':pk,'slot2':qk,'day':rk,'teacher':teacher})
def upload(request):
    if(request.method=="POST"):
        file = (request.FILES['file'])
        xls = pd.ExcelFile(file) # use r before absolute file path 

        sheetX = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

        var1 = sheetX

        print(var1[1:]) #1 is the row number...
    return render(request,'upload.html')
    #read file from web?

