# Generated by Django 3.0 on 2020-01-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0010_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Imagedb',
        ),
    ]