from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Libreria(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)

    def __str__(self):
        return self.title