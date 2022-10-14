from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from omnicommon.admin import BaseUUIDAdmin, SlugSearch
from urlshort.models import URLShort


@admin.register(URLShort)
class URLShortAdmin(BaseUUIDAdmin):
    list_display = [
        'uuid',
        'original_url',
        'slug',
        'slug_url',
    ]

    list_filter = [
        SlugSearch,
        'created_at',
        'modified_at',
    ]

    list_per_page = settings.LIST_PER_PAGE

    def slug_url(self, row):
        url = f'{settings.LOCAL_DOMAIN_NAME}{row.slug}'
        return format_html(
            u'<a href="{}" style="margin:auto; text-align:left; display:block;" target="popup"><i class="fa fa-external-link" aria-hidden="true"> {}</i></a>',
            url, url)
