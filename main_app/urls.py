from django.urls import path
from . import views

urlpatterns  = [
    #dogs
    path('', views.dogs, name = 'index'),
    path('<int:dog_id>/', views.dog_details, name='details'),
    path('<int:pk>/delete', views.DogDelete.as_view(), name = 'delete_dog'),
    path('<int:pk>/update/', views.DogUpdate.as_view(), name = 'update_dog'),
    path('add_dog', views.DogCreate.as_view(), name = 'create_dog'),
    path('<int:dog_id>/add_feeding', views.add_feeding, name = 'add_feeding'),
    #registration
    path('accounts/signup/', views.signup, name='signup')
]