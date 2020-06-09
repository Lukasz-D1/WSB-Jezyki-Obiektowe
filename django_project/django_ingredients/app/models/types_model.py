from django.db import models
from django.urls import reverse


class Type(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('type_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.name)
