from django.shortcuts import render
from django.http import HttpResponse

# Matrix template views
def index(request):
    return render(request, 'app/index.html')

def charts(request):
    return render(request, 'app/charts.html')

def widgets(request):
    return render(request, 'app/widgets.html')

def tables(request):
    return render(request, "app/tables.html")

def grid(request):
    return render(request, "app/grid.html")

def form_basic(request):
    return render(request, "app/form_basic.html")

def form_wizard(request):
    return render(request, "app/form_wizard.html")

def buttons(request):
    return render(request, "app/buttons.html")

def icon_material(request):
    return render(request, "app/icon-material.html")

def icon_fontawesome(request):
    return render(request, "app/icon-fontawesome.html")

def elements(request):
    return render(request, "app/elements.html")

def gallery(request):
    return render(request, "app/gallery.html")

def invoice(request):
    return render(request, "app/invoice.html")

def chat(request):
    return render(request, "app/chat.html")

