# Generated by Django 3.1 on 2021-02-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('add', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mob_no', models.BigIntegerField()),
            ],
        ),
    ]