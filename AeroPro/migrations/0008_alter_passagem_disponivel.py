# Generated by Django 5.0.1 on 2024-01-31 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AeroPro', '0007_passagem_disponivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passagem',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]