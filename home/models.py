from django.db import models

# Create your models here.


class Catalog(models.Model):
    title_ru = models.CharField(max_length=100)
    img = models.ImageField(upload_to='home/img')
    title_en = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return self.title_ru
