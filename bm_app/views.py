from django.shortcuts import render

# Create your views here.
def home_page_bm(request):
    return render(request, 'index.html')

def capitulos(request):
    return render(request, 'capitulos.html')

def graficos(request):
    return render(request, 'graficos.html')

