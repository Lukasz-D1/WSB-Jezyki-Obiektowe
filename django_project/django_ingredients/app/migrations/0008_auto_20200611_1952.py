# Generated by Django 3.0.7 on 2020-06-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200611_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
