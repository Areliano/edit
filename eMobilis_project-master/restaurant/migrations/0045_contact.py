# Generated by Django 4.2.7 on 2023-11-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0044_testimony_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='text1', max_length=500)),
                ('address', models.CharField(default='text1', max_length=500)),
                ('phone', models.CharField(default='text1', max_length=500)),
                ('email', models.CharField(default='text1', max_length=500)),
                ('website', models.CharField(default='text1', max_length=500)),
            ],
        ),
    ]
