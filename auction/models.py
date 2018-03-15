from django.contrib.auth.models import User
from django.db import models


class Lot(models.Model):
    OPENED = 'opened'
    CLOSED = 'closed'
    CANCELED = 'canceled'
    STATUS_CHOICES = (
        (OPENED, 'Открыт'),
        (CLOSED, 'Закрыт'),
        (CANCELED, 'Отменен'),
    )
    name = models.CharField(max_length=500, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='lots/%Y/%m/%d/', verbose_name='Изображение')
    start = models.DateTimeField(verbose_name='Начало торгов')
    finish = models.DateTimeField(verbose_name='Окончание торгов')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=OPENED, verbose_name='Статус')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Победитель')
    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, verbose_name='Лот')
    amount = models.IntegerField(verbose_name='Сумма')
    inserted_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    def __str__(self):
        return "#{id}".format(id=self.id)

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'
