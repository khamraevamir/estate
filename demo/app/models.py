

from django.db import models


class Flat(models.Model):
    title = models.CharField('Загаловок', max_length=256)
    content = models.TextField('Описание')
    price_usd = models.IntegerField('Цена в долларах', default=0)
    rooms = models.IntegerField('Кол-во комнат', default=0)
    square = models.IntegerField('Площадь', default=0)
    floor_number = models.IntegerField('Этаж дома', default=0)
    floor = models.IntegerField('Этажность', default=0)
    BUILDING_TYPE = (
        ('V1', ('Панельная')),
        ('V2', ('Кирпичная')),
        ('V3', ('Древесная')),
    )
    building_type = models.CharField('Тип строения', max_length=300, choices = BUILDING_TYPE, null=True)
    PLAN = (
        ('V1', ('Раздельная')),
        ('V2', ('Смежная')),
        ('V3', ('Раздельно-смежная')),
    )
    plan = models.CharField('Планировка', max_length=300, choices = PLAN, null=True)


    ceiling = models.IntegerField('Высота потолка', default=0)
    
    REPAIR = (
        ('V1', ('Евроремонт')),
        ('V2', ('Средний')),
        ('V3', ('Старый')),
        ('V4', ('Требует ремонта')),
        ('V5', ('Коробка')),
    )
    repaiir = models.CharField('Ремонт', max_length=300, choices = REPAIR, null=True)
    bathroom = models.BooleanField('Санузел', default=False)
    furniture = models.BooleanField('Мебилирован', default=False)
    address = models.TextField('Адрес')

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


    def __str__(self):
        return self.title


class NewFlat(models.Model):
    title = models.CharField('Загаловок', max_length=256)
    content = models.TextField('Описание')
    price_uzs = models.IntegerField('Цена в сумах', default=0)
    price_usd = models.IntegerField('Цена в долларах', default=0)
    rooms = models.IntegerField('Кол-во комнат', default=0)
    square = models.IntegerField('Площадь', default=0)
    floor_number = models.IntegerField('Этаж дома', default=0)
    floor = models.IntegerField('Этажность', default=0)
    plan = models.BooleanField('Планировка', default=False)
    bathroom = models.BooleanField('Санузел', default=False)
    ceiling = models.IntegerField('Высота потолка', default=0)
    address = models.TextField('Адрес')


class Home(models.Model):
    title = models.CharField('Загаловок', max_length=256)
    content = models.TextField('Описание')
    price_uzs = models.IntegerField('Цена в сумах', default=0)
    price_usd = models.IntegerField('Цена в долларах', default=0)
    rooms = models.IntegerField('Кол-во комнат', default=0)
    square = models.IntegerField('Площадь', default=0)
    floor_number = models.IntegerField('Этаж дома', default=0)
    plan = models.BooleanField('Планировка', default=False)
    bathroom = models.BooleanField('Санузел', default=False)
    ceiling = models.IntegerField('Высота потолка', default=0)
    address = models.TextField('Адрес')
    furniture = models.BooleanField('Мебилирован', default=False)
    total_square = models.IntegerField('Общая Площадь', default=0)
    house_square = models.IntegerField('Жилая Площадь', default=0)
    electricity = models.BooleanField('Электричество', default=False)
    gas = models.BooleanField('Газ', default=False)
    heating = models.BooleanField('Отопление', default=False)
    water = models.BooleanField('Вода', default=False)
    sewerage = models.BooleanField('Канализация', default=False)
    repair = models.BooleanField('Ремонт', default=False)
    BUILDING_TYPE = (
        ('V1', ('Variant1')),
        ('V2', ('Variant2')),
    )
    building_type = models.CharField('Ремонт', max_length=300, choices = BUILDING_TYPE, null=True)


class Commercial(models.Model):
    title = models.CharField('Загаловок', max_length=256)
    content = models.TextField('Описание')
    price_uzs = models.IntegerField('Цена в сумах', default=0)
    price_usd = models.IntegerField('Цена в долларах', default=0)
    rooms = models.IntegerField('Кол-во комнат', default=0)
    square = models.IntegerField('Площадь', default=0)
    floor_number = models.IntegerField('Этаж дома', default=0)
    floor = models.IntegerField('Этажность', default=0)
    plan = models.BooleanField('Планировка', default=False)
    bathroom = models.BooleanField('Санузел', default=False)
    ceiling = models.IntegerField('Высота потолка', default=0)
    address = models.TextField('Адрес')
    availibility = models.BooleanField('Availibility', default=False)
    parking = models.BooleanField('Парковка', default=False)




class Land(models.Model):
    title = models.CharField('Загаловок', max_length=256)
    content = models.TextField('Описание')
    price_uzs = models.IntegerField('Цена в сумах', default=0)
    price_usd = models.IntegerField('Цена в долларах', default=0)
    address = models.TextField('Адрес')
    square = models.IntegerField('Площадь', default=0)
    availibility = models.BooleanField('Availibility', default=False)




