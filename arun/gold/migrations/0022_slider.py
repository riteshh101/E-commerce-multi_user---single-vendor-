# Generated by Django 3.0 on 2020-02-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0021_delete_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
    ]