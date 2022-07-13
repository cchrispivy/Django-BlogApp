from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'Donec rhoncus magna nec sollicitudin congue. Maecenas ultrices quam et risus placerat, ac convallis enim dignissim. Etiam suscipit volutpat nunc quis sagittis. Aliquam felis enim, auctor in varius quis, auctor non urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.',
        'image': 'https://user-images.githubusercontent.com/108819425/178132228-cfd33b01-36b9-4128-9ad0-f50cf3290b71.jpg',
        'date_posted': 'August 27, 2022'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
	'image': 'https://user-images.githubusercontent.com/108819425/178132228-cfd33b01-36b9-4128-9ad0-f50cf3290b71.jpg',
        'date_posted': 'August 28, 2022'
    },
    {
        'author': '',
        'title': '',
        'content': '',
	'image': '',
        'date_posted': ''
    },
    {
        'author': '',
        'title': '',
        'content': '',
	'image': '',
        'date_posted': ''
    },
]



# Matrix template views
def index(request):
    context = {
        'posts': posts,
        'iterator': range(1,4)
    }
    return render(request, 'app/index.html', context)

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

