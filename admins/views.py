from django.shortcuts import render, redirect
from users.models import Reg_Details


def admin_login(request):
    if request.method == "POST":

        username = request.POST["admin"]
        password = request.POST["password"]

        if username == "admin" and password == "admin":
            return redirect("userdetails")

        else:
            return render(
                request,
                "adminlogin.html",
                {"msg": "Invalid username or password"}
            )

    return render(request, "adminlogin.html")

def userdetails(request):
    users = Reg_Details.objects.all()

    return render(
    request,
    "user_details.html",
    {"users": users}
)