from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def catalog_list(request):
    return HttpResponse('Тут будет список услуг и товаров')


def catalog_detail(request, pk):
    return HttpResponse(f'Тут будет описание выбранной услуги/товара - {pk}\n '
                        f'\n {request}'
                        f'{HttpResponse.status_code}')

