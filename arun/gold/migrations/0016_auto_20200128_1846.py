# Generated by Django 3.0 on 2020-01-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0015_auto_20200113_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
