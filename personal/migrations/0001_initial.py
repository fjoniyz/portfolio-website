# Generated by Django 3.2.7 on 2021-09-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=150)),
            ],
        ),
    ]
