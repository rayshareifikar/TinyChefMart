# Generated by Django 5.1.1 on 2024-09-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_producttinychef_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttinychef',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
