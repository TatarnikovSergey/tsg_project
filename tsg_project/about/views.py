from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def description(request):
    template = 'about/about.html'
    # return HttpResponse('О проекте')
    return render(request, template)