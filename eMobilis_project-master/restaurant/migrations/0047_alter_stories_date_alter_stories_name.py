# Generated by Django 4.2.7 on 2023-11-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0046_rename_text2_stories_date_rename_text1_stories_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='date',
            field=models.CharField(default='text2', max_length=500),
        ),
        migrations.AlterField(
            model_name='stories',
            name='name',
            field=models.CharField(default='text1', max_length=500),
        ),
    ]
