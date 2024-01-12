from django.shortcuts import render, redirect
from .models import User, CUSTOMER, FREELANCER
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    data = request.POST
    login = data.get("login")
    email = data.get("email")
    password1 = data.get("password1")
    password2 = data.get("password2")
    role_freelance = data.get("freelance")
    condition_check = data.get("contidion_check")
    news_check = data.get("news_check")

    if request.method == 'POST':
        user = User.objects.filter(username = login).last()
        if user :
            messages.error(request, "Bunday foydalanuvchi mavjud")
            return redirect("sign_up")
        if not condition_check and not news_check:
            messages.info(request, "Shartlarga rozilik bildiring")
            return redirect("sign_up")
        if password1 != password2:
            messages.warning(request, "Parollar bir biriga mos emas")
            return redirect("sign_up")
        if role_freelance:
            user = User.objects.create(
                role = FREELANCER,
                username = login,
                email = email,
                password = make_password(password1)
            )
            return redirect("sign_in")
        else:
            user = User.objects.create(
                role = CUSTOMER,
                username = login,
                email = email,
                password = make_password(password1)
            )
            return redirect("sign_in")

        return redirect("home")
    return render(request, "sign_up.html")


def sign_in(request):
    data = request.POST
    username = data.get("login")
    password = data.get("password")
    
    if request.method == 'POST':
        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, "Email yoki parol xato!")
            return redirect("sign_in")

        if not user.is_activated:
            login(request, user)
            return redirect("activate")
        login(request, user)
        return redirect("home")
    return render(request, "sign_in.html")


def activate(request):
    data = request.POST
    if request.method == "POST":
        user = User.objects.filter(username=request.user).first()
        user.avatar = request.FILES.get("resume")
        user.first_name = data.get('firstname')
        user.last_name = data.get('lastname')
        user.is_activated = True
        user.save()
        return redirect("home")
    return render(request, 'activate.html')


def sign_out(request):
    logout(request)
    return redirect("sign_in")