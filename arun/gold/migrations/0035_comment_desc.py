# Generated by Django 3.1.2 on 2021-01-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0034_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='desc',
            field=models.TextField(default=0),
        ),
    ]
