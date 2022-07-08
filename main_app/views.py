from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Dog

def dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dog_details(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/details.html', {'dog':dog})

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    successurl = '/'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/'
