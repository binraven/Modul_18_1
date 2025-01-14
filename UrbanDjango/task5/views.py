from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

users = ["alex", "tim", "bob"]
info = {}

def sign_up_by_html(request):
    global users, info

    if "username" in info:
        info.pop("username")
    if "form" in info:
        info.pop("form")
    if "error" in info:
        info.pop("error")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
        elif int(age) < 18:
            info["error"] = "Вы должны быть старше 18"
        elif username.lower() in users:
            info["error"] = "Пользователь уже существует"
        else:
            users.append(username.lower())
            info["username"] = username
    return render(request, "fifth_task/registration_page.html", info)


def sign_up_by_django(request):
    global users, info
    if "form" in info:
        info.pop("form")
    if "username" in info:
        info.pop("username")
    if "error" in info:
        info.pop("error")
    if request.method == "POST":
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            if password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif int(age) < 18:
                info["error"] = "Вы должны быть старше 18"
            elif username.lower() in users:
                info["error"] = "Пользователь уже существует"
                print(info["error"])
            else:
                users.append(username.lower())
                info["username"] = username
                info["form"] = form


    form = UserRegister()
    info["form"] = form
    print(users)
    return render(request, "fifth_task/registration_page.html", info)

