from django.db import models

class Libreria(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField
    created_at = models.DateField
    updated_at = models.DateField

    def __str__(self):
        return self.title