# Generated by Django 5.1.1 on 2024-09-13 14:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_producttinychef_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttinychef',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
