# Generated by Django 4.0 on 2022-08-07 08:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='national_no',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(code='invalid_national_number', message='National number must be numeric', regex='^[0-9]*$')], verbose_name='National number'),
        ),
    ]
