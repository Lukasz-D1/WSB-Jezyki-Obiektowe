# Generated by Django 3.0.7 on 2020-06-11 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200611_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrients',
            name='ingredient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Ingredient'),
        ),
    ]
