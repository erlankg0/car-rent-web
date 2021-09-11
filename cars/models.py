from django.db import models
import datetime

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
        ('CH', 'Чуйская область'),
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
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    FUEL_TYPE_CHOICE = (
        ('BNZ', 'Бензин'),
        ('DZL', 'Дизель'),
        ('B-G', 'Бензин-Газ'),
        ('ELC', 'Электро'),

    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    TRANSMISSION = (
        ('MN', 'MANUAL'),
        ('AU', "AUTO/ROBOT"),
    )
    year_choice = []
    for r in range(1970, (datetime.datetime.now().year + 1)):
        year_choice.append((r, r))

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100, choices=COLOR_CHOICE)
    model = models.CharField(max_length=100)
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(choices=CONDITION_AUTO, max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    car_image = models.ImageField(upload_to='car_image/%Y/%m/%d')
    car_image_1 = models.ImageField(upload_to='car_image/%Y/%m/%d', blank=True)
    car_image_2 = models.ImageField(upload_to='car_image/%Y/%m/%d', blank=True)
    car_image_3 = models.ImageField(upload_to='car_image/%Y/%m/%d', blank=True)
    car_image_4 = models.ImageField(upload_to='car_image/%Y/%m/%d', blank=True)
    features = models.CharField(max_length=100, choices=features_choices)
    body_style = models.CharField(max_length=100, choices=BODY_STYLE_CHOICE)
    engine = models.FloatField()
    fuel_type = models.CharField(max_length=100, choices=FUEL_TYPE_CHOICE)
    transmission = models.CharField(max_length=255, choices=TRANSMISSION)
    interior = models.CharField(max_length=255)
    miles = models.PositiveIntegerField()
    doors = models.CharField(max_length=255, default='4', choices=door_choices)
    passengers = models.IntegerField(default=3, )
    vin_no = models.CharField(max_length=17)
    # millage = models.IntegerField()
    # no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.car_title
