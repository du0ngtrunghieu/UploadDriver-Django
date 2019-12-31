from django.shortcuts import render
from .models import Map

# Create your views here.
def Home(request):
    c = Map.objects.all()
    context = {
        "c":c
    }
    return render(request,'index.html',context)