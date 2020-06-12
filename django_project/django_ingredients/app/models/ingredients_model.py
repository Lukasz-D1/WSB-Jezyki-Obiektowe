from django.db import models
from django.urls import reverse
from app.models.types_model import Type
from django.contrib.auth.models import User


class Ingredient(models.Model):
    AWAITING = 'OC'
    ACCEPTED = 'AC'
    REJECTED = 'RE'
    STATUS = [
        (AWAITING, 'Oczekujacy'),
        (ACCEPTED, 'Zaakceptowany'),
        (REJECTED, 'Odrzucony'),
    ]

    id = models.AutoField(db_index=True, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS, default=AWAITING)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('ingredient_detail', kwargs={'pk': self.id})