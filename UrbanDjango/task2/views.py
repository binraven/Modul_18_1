from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def func_index(request):
    return render(request,"second_task/index2.html")

class class_index(TemplateView):
    template_name = "second_task/index1.html"
