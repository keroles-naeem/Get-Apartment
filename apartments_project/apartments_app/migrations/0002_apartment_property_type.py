# Generated by Django 5.1.4 on 2024-12-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='property_type',
            field=models.CharField(choices=[('villa', 'Villa'), ('apartment', 'Apartment'), ('townhouse', 'Townhouse')], default='apartment', max_length=20),
        ),
    ]
