# Generated by Django 3.1 on 2021-02-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindb',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
    ]