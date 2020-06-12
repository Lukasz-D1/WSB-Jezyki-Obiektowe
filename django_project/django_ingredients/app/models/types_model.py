from django.db import models


class Type(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)
