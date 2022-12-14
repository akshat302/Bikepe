# Generated by Django 3.2.11 on 2022-11-03 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stock', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelNumber', models.CharField(max_length=20)),
                ('purchaseDate', models.DateTimeField(null=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('warranty', models.DateTimeField(null=True)),
                ('price', models.FloatField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikerrr.bikecategory')),
            ],
        ),
    ]
