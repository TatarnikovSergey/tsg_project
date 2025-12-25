from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
data = [
    {'id': 1, 'title': 'Услуга или товар номер 1'},
    {'id': 2, 'title': 'Услуга или товар номер 2'},
]

def catalog_list(request):
    context = {'data': data}
    return render(request, 'catalog/list.html', context)


def catalog_detail(request, pk):
    detail = next((i for i in data if i['id'] == pk), None)
    context = {'detail': detail}
    return render(request, 'catalog/detail.html', context)


