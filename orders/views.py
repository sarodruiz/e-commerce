import json
from .models import User, Pizza, OrderItem, Order
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
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
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
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

@login_required
@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("id")
        item = Pizza.objects.get(pk=item_id)

        try:
            order = Order.objects.get(user=request.user, placed=False)
        except Order.DoesNotExist:
            order = None

        if order is not None:
            try:
                order_item = order.items.get(item__id=item.id)
            except OrderItem.DoesNotExist:
                order_item = None

            if order_item is not None:
                order_item.quantity = order_item.quantity + 1
                order_item.save()
            else:
                order_item = OrderItem.objects.create(item=item)
                order.items.add(order_item)
        else:
            order_item = OrderItem.objects.create(item=item)
            order = Order.objects.create(user=request.user)
            order.items.add(order_item)
            order.save()

        items = order.items.all()
        #return JsonResponse([item.serialize() for item in items], safe=False)
        return JsonResponse({
            "status": "success"
            })

@csrf_exempt
@login_required
def remove_from_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("id")
        item = Pizza.objects.get(pk=item_id)
        
        try:
            order = Order.objects.get(user=request.user, placed=False)
        except Order.DoesNotExist:
            order = None

        if order is not None:
            try:
                order_item = order.items.get(item__id=item.id)
            except OrderItem.DoesNotExist:
                order_item = None
            if order_item is not None:
                order.items.remove(order_item)

        items = order.items.all()
        #return JsonResponse([item.serialize() for item in items], safe=False)
        return JsonResponse({
            "status": "success"
            })

@login_required
def cart(request):
    try:
        order = Order.objects.get(user=request.user, placed=False)
    except Order.DoesNotExist:
        order = None

    return render(request, "orders/cart.html", {
        "order": order
    })
