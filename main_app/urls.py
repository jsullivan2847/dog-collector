from django.urls import path
from . import views

urlpatterns  = [
    path('', views.dogs, name = 'index'),
    path('<int:dog_id>/', views.dog_details, name='details'),
    path('<int:pk>/delete', views.DogDelete.as_view(), name = 'delete_dog'),
    path('add_dog', views.DogCreate.as_view(), name = 'create_dog'),
]