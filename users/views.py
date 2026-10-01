from django.shortcuts import render,redirect
from .models import Reg_Details


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":

        name = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        address = request.POST["address"]

        Reg_Details.objects.create(
            name=name,
            password=password,
            email=email,
            address=address
        )
        return redirect("login")

    return render(request, "register.html")

def login(request):

    if request.method == "POST":

        name = request.POST["username"]
        password = request.POST["password"]

        try:
            user = Reg_Details.objects.get(
                name=name,
                password=password
            )

            return render(
                request,
                "user_dashboard.html"
            )

        except Reg_Details.DoesNotExist:

            return render(
                request,
                "login.html",
                {"msg": "Invalid username or password"}
            )

    return render(request, "login.html")

def logout(request):
    return render(request,"home.html")