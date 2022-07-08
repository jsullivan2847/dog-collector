from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    age = models.IntegerField()

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

    def __str__(self):
        return f'{self.name} is a {self.color} {self.breed}'

    def get_absolute_url(self):
        return reverse('details', kwargs={'dog_id': self.id})

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

