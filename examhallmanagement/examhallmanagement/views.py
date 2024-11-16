from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from timebale.models import Timetable

def home(request):
    return render(request, 'index.html')

def sendmail(request):
     subject = 'welcome to GFG world'
     message = f'Hi , thank you for registering in geeksforgeeks.'
     email_from = settings.EMAIL_HOST_USER
     recipient_list = ["deepakviji123@gmail.com", ]
     send_mail( subject, message, email_from, recipient_list )   
     return HttpResponse("ok")

def selection(request):
    if(request.POST):
        login_data = request.POST.dict()
        start = login_data.get("sslot")
        end = login_data.get("eslot")
        day= login_data.get("day")
        s="slot"+start
        teacher = Timetable.objects.filter(
                day=day
            )
        print(teacher)
        return HttpResponse(teacher)

def upload(request):
    if request.method == "post":
        print("ldleee")
        #print(request.POST.file)
    return render(request,'upload.html')








