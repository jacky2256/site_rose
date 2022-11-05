from django.shortcuts import render
from .models import Catalog
# Create your views here.


def home(request):
    rose_types = Catalog.objects.all()

    return render(request, 'home/home.html', {'rose_types': rose_types})
