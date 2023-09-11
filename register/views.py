from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials!")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["firstname"]
        sur_name = request.POST["surname"]
        user_name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST['password1']
        password2 = request.POST["password2"]
        
        if User.objects.filter(username=user_name).exists():
            messages.info(request, "Username is already taken!")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,  "Email already taken!")
            return redirect('register')
        elif password1 != password2:
            messages.info(request, "Passwords are not matching!")
            return redirect('register')
        else:
            user = User.objects.create_user(username=user_name, password=password2, email=email, first_name=first_name, last_name=sur_name)
            user.save()
            return redirect("login")

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')