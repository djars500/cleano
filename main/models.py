from collections import Counter
from django.db import models
from django.contrib.auth.models import User


class Courier(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    in_work = models.BooleanField( 'Занятость' , default=False)


    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Курьера'
        verbose_name_plural = 'Курьеры'


class Usluga(models.Model):
    name = models.CharField('Наименование услуги',max_length=255)
    price = models.CharField('Цена', max_length=255)
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

class Place(models.Model):
    name = models.CharField("Помещение", max_length=255)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

class Zayavka(models.Model):
    
    status = (
        ('В ожидании', 'В ожидании'),
        ('На отработке', 'На отработке'), 
        ('Заказ выполнен', 'Заказ выполнен')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль', null=True, blank=True)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, verbose_name='Курьер',null=True, blank=True)
    phone = models.CharField('Номер телефона',max_length=11, null=True, blank=True)
    address = models.CharField('Адрес дома', max_length=255, blank=True, null=True)
    metr = models.IntegerField('Площадь дома(м²)', null=True, blank=True)
    statuc = models.CharField('Статус заявки', max_length=255 , choices=status, blank=True, null=True, default='В ожидании')
    house = models.ForeignKey(Place, on_delete=models.CASCADE,verbose_name="Выберите помещение" ,null=True, blank=True)
    usluga = models.ForeignKey(Usluga, on_delete=models.CASCADE, verbose_name='Услуга', null=True, blank=True)
    total = models.CharField('Сумма', max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.courier} {self.created_at}'

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def save(self, *args, **kwargs):
        self.total = self.metr * int(self.usluga.price)
        super().save(*args, **kwargs)

    

class Contact(models.Model):
    phone = models.CharField('Номер телефона' ,max_length=12)
    name = models.CharField('Имя', max_length=255)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'


class Result(models.Model):
    img_one = models.ImageField('Фото до', upload_to='img_one')
    img_two = models.ImageField('Фото после', upload_to='img_two')

    def __str__(self):
        return f'До и после'

    class Meta:
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Наши работы'