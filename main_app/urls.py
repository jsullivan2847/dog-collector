from django.urls import path
from . import views

urlpatterns  = [
    #dogs
    path('', views.home, name = 'home'),
    path('dogs/', views.dogs, name = 'index'),
    path('<int:dog_id>/', views.dog_details, name='details'),
    path('<int:pk>/delete', views.DogDelete.as_view(), name = 'delete_dog'),
    path('<int:pk>/update/', views.DogUpdate.as_view(), name = 'update_dog'),
    path('add_dog', views.DogCreate.as_view(), name = 'create_dog'),
    path('<int:dog_id>/add_feeding', views.add_feeding, name = 'add_feeding'),
    #registration
    path('accounts/signup/', views.signup, name='signup'),
    #toys
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>', views.ToyDetails.as_view(), name='toys_details'),
    path('toys/add', views.AddToy.as_view(), name='add_toy'),
    path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    #photos
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name="add_photo")
]