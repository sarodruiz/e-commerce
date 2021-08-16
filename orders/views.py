from orders.models import Pizza
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
#from django.contrib.auth.models import User
from .models import User

# Create your views here.
def index(request):
    #return HttpResponse("Project 3: TODO")
    return render(request, "orders/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            print("INVALID CREDENTIALS")
            return render(request, "orders/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "orders/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        first_name = request.POST["first"]
        last_name = request.POST["last"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "orders/register.html", {
                "message": "Passwords must match."
            })
        try:
            #user = User.objects.create_user(username, first_name, last_name, email, password)
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
        except IntegrityError:
            return render(request, "order/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/register.html")

def menu(request):
    items = Pizza.objects.all()
    return render(request, "orders/menu.html", {
        "items": items
    })