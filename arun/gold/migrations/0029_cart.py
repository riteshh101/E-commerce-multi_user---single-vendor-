# Generated by Django 3.1.2 on 2021-01-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0028_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images')),
                ('idd', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
