from django.contrib import admin
from django.utils.safestring import mark_safe

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    def get_img(self, obj):
        return mark_safe(f'<img src={obj.car_image.url} width="70" style="border-radius: 50px;">')

    list_display = (
        'get_img',
        'car_title',
        'model',
        'fuel_type',
        'state',
        'price',
        'is_featured',

    )
    list_display_links = (
        'get_img',
        'car_title',
        'model',
        'state',
        'price',
    )
    list_editable = ('is_featured',)
    list_filter = (
        'fuel_type',
        'model',
    )
    search_fields = (
        'car_title',
        'model',
        'vin_no',
    )


admin.site.register(Car, CarAdmin)
# Register your models here.
