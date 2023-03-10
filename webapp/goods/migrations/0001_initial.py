# Generated by Django 4.1.7 on 2023-03-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Модель')),
                ('cost', models.FloatField(max_length=15, verbose_name='Цена')),
                ('avail', models.IntegerField(verbose_name='Наличие')),
                ('pic', models.CharField(max_length=100, verbose_name='Ссылка на фото')),
                ('company', models.CharField(max_length=100, verbose_name='Производитель')),
                ('image', models.ImageField(upload_to='images', default='iphone_x.jpg'))
            ],
        ),
    ]
