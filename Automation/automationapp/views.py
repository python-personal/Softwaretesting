from django.shortcuts import render,redirect
from django.contrib import messages
from automationapp.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def indexview(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(name,email,message)
        try:
            if (len(name) ==0 or len(email) ==0 or len(message)==0):
                return render(request,"automationapp/index.html")
            else:
                user=enquiry.objects.create(name=name,email=email,message=message)
                user.save()
                # messages.success(request,"Request Recieved, We Will Get Back Soon!!")
                return render(request,"automationapp/index.html",{'message': "Request Recieved, We Will Get Back To You Soon!!",'successful_submit':True})
        except:
            # messages.error(request,"Unable to send query!!")
            return HttpResponseRedirect("/")
    else:
        return render(request,"automationapp/index.html")

def home(request):
    return render(request,"automationapp/home.html")
def functional_view(request):
    return render(request,"automationapp/functional.html")

def performance_view(request):
    return render(request,"automationapp/performance.html")

def API_view(request):
    return render(request,"automationapp/api.html")

def integration_view(request):
    return render(request,"automationapp/integration.html")

def AI_view(request):
    return render(request,"automationapp/AI.html")

def robotic_view(request):
    return render(request,"automationapp/robotic.html")
