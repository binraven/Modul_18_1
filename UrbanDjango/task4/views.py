from django.shortcuts import render

# Create your views here.
def menu (request):
    pagename = "Главная страница"
    context = {
        "pagename": pagename
    }
    return render(request, "fourth_task/menu.html", context)

def pie (request):
    pagename = "Пироги"
    pies = {1: "С рыбой", 2: "С мясом", 3: "Сюрприз"}
    context = {
        "pies": pies,
        "pagename": pagename
    }

    return render(request, "fourth_task/pie.html", context)

def soup (request):
    pagename = "Супы"
    context = {
        "pagename": pagename
    }
    return render(request, "fourth_task/soup.html", context)
