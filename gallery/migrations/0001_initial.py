# Generated by Django 4.0.4 on 2022-05-28 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('photo_url', models.CharField(max_length=200)),
                ('photo_image', models.ImageField(blank=True, upload_to='photo/')),
                ('category', models.ManyToManyField(to='gallery.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.user')),
            ],
        ),
    ]
