from django.db import models
from app.models.ingredients_model import Ingredient
from django.contrib.auth.models import User


class Nutrients(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    calories_per_100g = models.IntegerField(default=0)
    fats_per_100g = models.IntegerField(default=0)
    protein_per_100g = models.IntegerField(default=0)
    carbs_per_100g = models.IntegerField(default=0)
