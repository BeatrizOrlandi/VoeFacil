# Generated by Django 5.0.1 on 2024-01-31 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AeroPro', '0006_alter_voo_comissario'),
    ]

    operations = [
        migrations.AddField(
            model_name='passagem',
            name='disponivel',
            field=models.BooleanField(default=0),
        ),
    ]