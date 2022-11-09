from django.shortcuts import render, get_object_or_404
from home import models as home_models
from . import models
from django.http import HttpResponse
# Create your views here.


def all_categories(request):

    rose_types = home_models.Catalog.objects.all()

    return render(request, 'catalog/all_categories.html', {'rose_types': rose_types})


def all_categ_roses(request):

    roses = models.Roses.objects.all()

    #roses = models.Roses.objects.filter(sort='флорибунда')

    return render(request, 'catalog/all_categ_roses.html', {'roses': roses})


def rose_description(request, roses_title):

    print(roses_title)
    rose = get_object_or_404(models.Roses, title=roses_title)
    #roses = models.Roses.objects.all()
    return render(request, 'catalog/rose_description.html', {'rose': rose})
