from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name