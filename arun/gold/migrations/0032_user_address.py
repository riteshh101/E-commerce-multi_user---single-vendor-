# Generated by Django 3.1.2 on 2021-01-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0031_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zip', models.IntegerField()),
            ],
        ),
    ]
