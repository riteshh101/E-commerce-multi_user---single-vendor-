# Generated by Django 3.0 on 2020-02-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0019_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=1000)),
                ('mobile', models.IntegerField()),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]
