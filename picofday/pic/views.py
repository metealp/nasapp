from django.shortcuts import render
from .models import Img
from django.utils import timezone

def index(request):
    imges = Img.objects.order_by("date")
    return render(request, 'pic/index.html', {"imges":imges})
