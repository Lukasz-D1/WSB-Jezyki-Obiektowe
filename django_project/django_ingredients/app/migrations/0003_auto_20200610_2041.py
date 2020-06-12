# Generated by Django 3.0.7 on 2020-06-10 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200610_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='calories_per_100g',
        ),
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('calories_per_100g', models.IntegerField(default=0)),
                ('fats_per_100g', models.IntegerField(default=0)),
                ('protein_per_100g', models.IntegerField(default=0)),
                ('carbs_per_100g', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ingredient')),
            ],
        ),
    ]