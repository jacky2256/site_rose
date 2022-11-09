from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('roses/', views.all_categ_roses, name='all_categ_roses'),

    # path('<int:roses_id>',
    #     views.rose_description, name='rose_description')
    path('<str:roses_title>',
         views.rose_description, name='rose_description')
]
