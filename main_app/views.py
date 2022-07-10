from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Dog, Toy, Photo
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid, boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'django-cat-collector-2847'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign up, try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def dogs(request):
    # # if not user == request.user:
    #     return redirect('login')
    dogs = Dog.objects.filter(user = request.user)
    return render(request, 'dogs/index.html', {'dogs': dogs})

@login_required
def dog_details(request, dog_id):
    dog = Dog.objects.get(id = dog_id)
    other_toys = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dogs/details.html', {
        'dog':dog, 'feeding_form': feeding_form,
        'toys': other_toys })

@login_required
def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('details', dog_id = dog_id)

@login_required
def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id = dog_id).toys.add(toy_id)
    return redirect('details', dog_id=dog_id)

def home(request):
    return render(request, 'home.html')

@login_required
def add_photo(request, dog_id):
    photo_file = request.FILES.get('photo_file', None)
    if photo_file:
        S3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
        S3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        photo = Photo(url=url,dog_id = dog_id)
        photo.save()
    except Exception as error:
        print("Error uploading photo", error)

    return redirect('details', dog_id = dog_id)

class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/'


class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = '__all__'


class ToyList(LoginRequiredMixin,ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetails(LoginRequiredMixin, DetailView):
    model = Toy
    template_name = 'toys/details.html'

class AddToy(LoginRequiredMixin, CreateView):
    model = Toy
    fields = ['name', 'color']

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'