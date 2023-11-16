from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Libreria(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title