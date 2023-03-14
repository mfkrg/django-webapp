from django.db import models
from django.contrib.auth.models import User


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


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    good = models.ForeignKey(to=Goods, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.good.title}'