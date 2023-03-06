from django.db import models

class Goods(models.Model):
    title = models.CharField('Модель', max_length=100)
    cost = models.FloatField('Цена', max_length=15)
    avail = models.IntegerField('Наличие')
    pic = models.CharField('Ссылка на фото', max_length=100)
    company = models.CharField('Производитель', max_length= 100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'