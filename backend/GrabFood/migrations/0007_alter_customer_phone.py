# Generated by Django 4.1.3 on 2025-01-16 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrabFood', '0006_alter_restaurant_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Enter a valid phone number with exactly 10 digits')]),
        ),
    ]
