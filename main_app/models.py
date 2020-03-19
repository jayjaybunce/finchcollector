from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.



class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return f'N:{self.name} C:{self.color} A:{self.age}'

    def get_absolute_url(self):
        return reverse("finches:detail", kwargs={"finch_id": self.id})
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


MEALS = (
    ('B','Breakfast'),
    ('L','Lunch'),
    ('D','Dinner'),
)
class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default = MEALS[0][0]
        )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'


