from asyncio.windows_events import NULL
import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def home_view(request):

    return render(request, 'index.html')

def signup_view(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        obj = Registered_users(Username = data['Name'], Email = data['Email'], DOB = data['DOB'], Password = data['Password'])
        obj.save()

        return redirect("http://127.0.0.1:8000/main/")

def signin_view(request):
    if request.method == "POST":
        data = request.POST
        row = Registered_users.objects.all()

        for i in row:
            if(i.Email == data['email'] and i.Password == data['password']):
                print("Found")
            else:
                print("not found")


        
        return redirect("http://127.0.0.1:8000/main/")