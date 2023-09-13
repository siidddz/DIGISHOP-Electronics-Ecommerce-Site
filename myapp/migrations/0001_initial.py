# Generated by Django 4.2 on 2023-04-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveSmallIntegerField()),
                ('address', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
