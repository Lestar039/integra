# Generated by Django 3.1.4 on 2020-12-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteData',
            fields=[
                ('url', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='URL')),
                ('status', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
