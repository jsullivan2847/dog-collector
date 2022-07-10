from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('toys_details', kwargs = {'pk': self.id})

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    toys = models.ManyToManyField(Toy)

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    def __str__(self):
        return f'{self.name} is a {self.color} {self.breed}'

    def get_absolute_url(self):
        return reverse('details', kwargs={'dog_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default = MEALS[0][0]
    )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"


    

