from django.db import models

# Create your models here.


class Roses(models.Model):
    title = models.CharField(max_length=100)
    sort = models.CharField(max_length=100, default='Флорибунда')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.ImageField(upload_to='categories/img')
    color = models.CharField(max_length=100, default='red')
    number_of_flowers = models.IntegerField(default=5)
    size_flowers = models.IntegerField(default=7)
    height = models.IntegerField(default=100)
    width = models.IntegerField(default=80)
    author = models.CharField(max_length=100, default='Peter J. James')
    year_made = models.IntegerField(default=2008)
    title_en = models.CharField(max_length=100, default='Eyes for You')
    city_made = models.CharField(max_length=100, default='Great Britain')
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.title
