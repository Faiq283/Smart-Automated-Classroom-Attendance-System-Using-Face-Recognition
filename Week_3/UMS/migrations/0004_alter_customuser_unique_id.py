# Generated by Django 3.2 on 2025-02-25 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UMS', '0003_customuser_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
