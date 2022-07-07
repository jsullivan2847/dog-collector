from django.shortcuts import render

from django.http import HttpResponse
from .models import Dog

def dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})
