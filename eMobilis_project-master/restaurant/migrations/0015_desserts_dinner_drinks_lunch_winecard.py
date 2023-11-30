# Generated by Django 4.2.7 on 2023-11-29 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_stories_rename_image_homepage_background_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desserts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image10', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image11', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image12', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('text10', models.CharField(default='text4', max_length=500)),
                ('text11', models.CharField(default='text5', max_length=500)),
                ('text12', models.CharField(default='text6', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image7', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image8', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image9', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('text7', models.CharField(default='text4', max_length=500)),
                ('text8', models.CharField(default='text5', max_length=500)),
                ('text9', models.CharField(default='text6', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image19', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image20', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image21', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('text19', models.CharField(default='text4', max_length=500)),
                ('text20', models.CharField(default='text5', max_length=500)),
                ('text21', models.CharField(default='text6', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image4', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image5', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image6', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('text4', models.CharField(default='text4', max_length=500)),
                ('text5', models.CharField(default='text5', max_length=500)),
                ('text6', models.CharField(default='text6', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Winecard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image16', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image17', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('image18', models.ImageField(default='menu.jpg', upload_to='menu')),
                ('text16', models.CharField(default='text4', max_length=500)),
                ('text17', models.CharField(default='text5', max_length=500)),
                ('text18', models.CharField(default='text6', max_length=500)),
            ],
        ),
    ]