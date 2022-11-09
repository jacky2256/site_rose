from django.shortcuts import render, get_object_or_404
from home import models as home_models
from . import models
from django.http import HttpResponse
# Create your views here.


def all_categories(request):

    rose_types = home_models.Catalog.objects.all()

    return render(request, 'catalog/all_categories.html', {'rose_types': rose_types})


def all_categ_roses(request):

    if request.GET.get('all'):
        roses = models.Roses.objects.all()
        return render(request, 'catalog/all_categ_roses.html', {'roses': roses})

    sort_key = list(request.GET.keys())
    print(sort_key[0])

    sort_ru = {
        'floribunda': 'флорибунда',
        'english': 'Розы английской селекции',
        'bardiurnie': 'Бардюрные (патио) розы',
        'pochvopocrovnie': 'Почвопокровные розы',
        'chainogibrid': 'чайно-гибридные',
        'shtampovie': 'Штамповые розы',
        'pletistie': 'Плетистые розы',
    }

    roses = models.Roses.objects.filter(sort=sort_ru.get(sort_key[0]))

    return render(request, 'catalog/all_categ_roses.html', {'roses': roses})


def rose_description(request, roses_title):

    print(roses_title)
    rose = get_object_or_404(models.Roses, title=roses_title)
    return render(request, 'catalog/rose_description.html', {'rose': rose})
