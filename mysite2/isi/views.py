from django.shortcuts import render

# Create your views here.

def isi(request):
    return render(request, "isi/isigame.html")