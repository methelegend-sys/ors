# Generated by Django 3.2.2 on 2021-06-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_delivery_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_data',
            name='new_del',
            field=models.FileField(upload_to=''),
        ),
    ]
