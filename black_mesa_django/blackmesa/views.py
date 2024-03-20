from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def enredo(request):
    return render(request, 'enredo.html')


