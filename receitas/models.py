from django.db import models

class Receita(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='receitas/images/', blank=True, null=True)