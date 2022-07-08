from django.db import models
from django.urls import reverse

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} is a {self.color} {self.breed}'

    def get_absolute_url(self):
        return reverse('details', kwargs={'dog_id': self.id})

