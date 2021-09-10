from django.contrib import admin
from django.utils.safestring import mark_safe

from pages.models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def get_img(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="40" style="border-radius: 50px;">')

    get_img.short_description = 'изображения'
    list_display = (
        'id',
        'get_img',
        'first_name',
        'last_name',
        'designation',
    )
    list_display_links = (
        'id',
        'get_img',
        'first_name',
        'last_name',
        'designation',
    )
    readonly_fields = ('get_img',)
    search_fields = (
        'first_name',
        'last_name',
        'designation',
    )


admin.site.register(Team, TeamAdmin)
