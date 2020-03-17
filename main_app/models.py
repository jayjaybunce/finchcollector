from django.db import models

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'N:{self.name} C:{self.color} A:{self.age}'

