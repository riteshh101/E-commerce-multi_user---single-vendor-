# Generated by Django 3.0 on 2020-01-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0013_auto_20200112_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.IntegerField(default=False),
        ),
    ]
