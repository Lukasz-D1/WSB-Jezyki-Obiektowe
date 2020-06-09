from django.db import models
from app.models.types_model import Type


class Ingredient(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)
