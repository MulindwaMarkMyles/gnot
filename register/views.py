from django.shortcuts import render
from .models import User


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # check if the user is in the database....

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        sur_name = request.POST["surname"]
        user_name = request.POST["username"]
        password = request.POST["password"]

    return render(request, "register.html")
