# Generated by Django 4.2.4 on 2023-08-19 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ling_toolkits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
            ],
        ),
    ]
