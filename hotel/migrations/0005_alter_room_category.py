# Generated by Django 4.2.7 on 2023-11-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('A25', 'Apt A25 1 Bedroom'), ('A01', 'Apt A01 2 Bedrooms'), ('A19', 'Apt A19 2 Bedrooms')], max_length=3),
        ),
    ]
