from django.shortcuts import render

# Create your views here.
def cooking (request):
    title = "Кулинарный портал"
    context = {
        "title" : title
    }
    return render(request, "third_task/cooking.html", context)

def pie (request):
    return render(request, "third_task/pie.html")

def soup (request):
    return render(request, "third_task/soup.html")