from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def inicio(request):
    return render(request, 'app/inicio.html')

def personajes(request):
    return render(request, 'app/personajes.html')

def items(request):
    return render(request, 'app/items.html')

def controles(request):
    return render(request, 'app/controles.html')

