# Generated by Django 4.2.2 on 2023-06-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('joiningdate', models.DateField()),
                ('gender', models.CharField(max_length=255)),
                ('qualifiation', models.CharField(max_length=255)),
                ('mobileno', models.CharField(max_length=255)),
            ],
        ),
    ]
