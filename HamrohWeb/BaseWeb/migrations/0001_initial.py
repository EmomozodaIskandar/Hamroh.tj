# Generated by Django 4.2.7 on 2023-11-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationName', models.CharField(max_length=128)),
                ('Country', models.CharField(default='Tajikistan', max_length=64)),
            ],
        ),
    ]
