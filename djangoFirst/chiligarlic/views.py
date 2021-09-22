from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def index(request):

    menus = MenuItem.objects.all()

    return render(request, "index.html", {'menus': menus})
