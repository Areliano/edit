# Generated by Django 4.2.7 on 2023-11-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0033_alter_aboutpage_img1_alter_aboutpage_img2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourmenu',
            name='btn',
            field=models.CharField(default='button', max_length=20),
        ),
    ]