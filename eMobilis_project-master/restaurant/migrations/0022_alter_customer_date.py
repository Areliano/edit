# Generated by Django 4.2.7 on 2023-11-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_alter_customer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.CharField(default='dd/mm/yyyy', max_length=10),
        ),
    ]
