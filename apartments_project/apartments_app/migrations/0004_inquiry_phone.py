# Generated by Django 5.1.4 on 2024-12-16 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments_app', '0003_remove_apartment_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]