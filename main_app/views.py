from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Dog
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        

def dogs(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dog_details(request, dog_id):
    dog = Dog.objects.get(id = dog_id)
    feeding_form = FeedingForm()
    return render(request, 'dogs/details.html', {
        'dog':dog, 'feeding_form': feeding_form })

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detais', dog_id = dog_id)

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    successurl = '/'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/'

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'
