from django.shortcuts import render

# Create your views here.
def home(request, index):
    return render(request, 'home.html', {})