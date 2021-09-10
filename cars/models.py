from django.db import models

# Create your models here.
""" Cars model 
car_title
city
state
color
model
year
condition
description
car_photo
car_photo_1
car_photo_2
car_photo_3
features
body_style
interior
miles
doors
passengers
vin_num
millage
fuel_type
is_featured
created_date

"""


class Car(models.Model):
    STATE_CHOICE = (
        ('CH', 'Чуйская область',
         # ('BH', 'Бишкек'),
         # ('TK', 'Токмок'),
         ),
        ('TL', 'Талаская область'),
        ('IS', 'Иссык-Кульская область'),
        ('NR', 'Нарынская область'),
        ('OS', 'Ошская область',),
        ('BT', 'Баткенская область'),
        ('DJ', 'Джалал Абадская область'),
    )
    COLOR_CHOICE = (
        ('RD', 'Красный'),
        ('BL', 'Синий'),
        ('YL', 'Жёлтый'),
        ('GR', 'Зелёный'),
        ('BK', 'Чёрный'),
        ('PG', 'Розовый'),
        ('WH', 'Белый'),
    )
    CONDITION_AUTO = (
        ('NW', 'Новая'),
        ('PR', 'Отличная'),
        ('GD', 'Хорошое'),
        ('BD', 'Удовлетворительно'),
    )
    BODY_STYLE_CHOICE = (
        ('SDN', 'Седан'),
        ('SRT', 'Спорт-Авто'),
        ('SUV', 'Внедорожник'),
        ('HTC', 'Хэтчбек'),
        ('PCP', 'Пикап'),
    )
    DOORS_CHOICE = (
        ('6', 'Шести дверная'),
        ('5', 'Пяти дверная'),
        ('4', 'Четырех дверная'),
        ('3', 'Трех дверная'),
        ('2', 'Двух дверная'),
        ('1', 'Одно дверная'),
        ('7', 'Больше 6 дверей'),
    )
    FUEL_TYPE_CHOICE = (
        ('BNZ', 'Бензин'),
        ('DZL', 'Дизель'),
        ('B-G', 'Бензин-Газ'),
        ('ELC', 'Электро'),

    )
    car_title = models.CharField(verbose_name='Названия авто.', max_length=255)
    state = models.CharField(max_length=2, choices=STATE_CHOICE, verbose_name='Выбор области')
    color = models.CharField(max_length=2, verbose_name='цвет', choices=COLOR_CHOICE)
    model = models.CharField(max_length=200, verbose_name='Модель авто')
    year = models.DateField(verbose_name='Дата авто', )
    body_style = models.CharField(verbose_name='Тип кузова', max_length=3, unique=True,
                                  help_text='Выбор кузова обязательно', choices=BODY_STYLE_CHOICE)
    fuel_type = models.CharField(verbose_name='Тип топливо', choices=FUEL_TYPE_CHOICE, max_length=3)
    kilometers = models.PositiveBigIntegerField(verbose_name='Пробег авто.')
    doors = models.CharField(verbose_name='Количество двере.', max_length=1, choices=DOORS_CHOICE)
    condition = models.CharField(verbose_name='Состояния авто', max_length=2, choices=CONDITION_AUTO)
    description = models.TextField(verbose_name='Описания авто', max_length=1000, help_text='Максимум 1000 символов')
    car_photo = models.ImageField(verbose_name='Фото авто', upload_to='car_photo/Y%/%m/%d', unique_for_date=True,
                                  help_text='Обязательно заполнения картинки!')
    car_photo_1 = models.ImageField(upload_to='car_photo_1/Y%/%m/%d', unique_for_date=True, blank=True, null=True)
    car_photo_2 = models.ImageField(upload_to='car_photo_2/Y%/%m/%d', unique_for_date=True, blank=True, null=True)
    car_photo_3 = models.ImageField(upload_to='car_photo_3/Y%/%m/%d', unique_for_date=True, blank=True, null=True)
    passengers = models.PositiveSmallIntegerField(verbose_name='Кол пассажиров.', default=0)
    is_featured = models.BooleanField(verbose_name='Рекомендации.', default=False)
    created_date = models.DateField(auto_now=True, verbose_name='Дата публикации.')

    def __str__(self):
        return self.car_title
