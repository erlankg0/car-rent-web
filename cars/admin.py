from django.contrib import admin
from django.utils.safestring import mark_safe

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    def get_img(self, obj):
        return mark_safe(f'<img src={obj.car_image.url} width="70" style="border-radius: 50px;">')

    list_display = (
        'get_img',
        'car_title',
        'state',
        'model',
        'price',

    )
    list_display_links = (
        'get_img',
        'car_title',
        'state',
        'model',
        'price',

    )


admin.site.register(Car, CarAdmin)
# Register your models here.
